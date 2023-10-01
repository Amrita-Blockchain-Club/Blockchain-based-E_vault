from flask import Flask, send_file , render_template, request, redirect, session, url_for
import socket
import tqdm
import subprocess
import os
import threading
import sys
import asyncio
import mongo_op as mongo
from Run_commands import get_only_cid, upload_to_ipfs
from serverdetails import SERVER_HOST, SERVER_PORT, BUFFER_SIZE, SEPARATOR
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'mysecretkey'

mongo = mongo.Mongo()

@app.route('/', methods=['GET', 'POST'])
async def download_file():
    if request.method == 'POST':

        public_key = request.form['public_key']
        file = request.files['file']

        filename = secure_filename(file.filename)

        directory = f"Storage/{public_key}"
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        file.save(filepath)

        if os.path.exists(filepath):
            response = await StartOperation(filepath, public_key)
            print(response)
            if response[1]:
                return render_template('result.html', cid=response[0], message='File already exists', status_code=200)
            else:
                return render_template('result.html', cid=response[0], message='File uploaded successfully', status_code=200)
        else:
            return 'File not found.'
    else:
        return render_template('download.html')


async def StartOperation(filepath, public_key) -> tuple:
        
        cid = await get_only_cid(filepath)
        status = await mongo.isFileExist(user=public_key, cid=cid)

        if status:
            print(f"[/] File already exists. CID: {cid}")
        else:
            # Upload the file to IPFS
            cid = await upload_to_ipfs(filepath)
            print(f"[+] File uploaded to IPFS. CID: {cid}")

            # Update mongodb
            result = await mongo.insert(user=public_key, cid=cid)

            if result:
                print("[+] MongoDB database updated successfully.")
            else:
                print("[-] An error occurred while updating the MongoDB database.")

        # Send response to the client
            try:
                delete = await delete_file(filepath)
                print(delete, "--> Delete status")
            except Exception as e:
                print(e)
                print("[-] An error occurred while deleting the file from the server.")
                return 'Error deleting file from server.'
            
        try:
            response = (cid, status)
            print(response)
            return response
        except:
            print("[-] An error occurred while sending the response to the client.")
            return (None, False)

async def delete_file(filepath) -> bool:
    os.remove(filepath)
    print(f"[+] File deleted from server. Filename: {filepath.split('/')[-1]}")
    return True



if __name__ == '__main__':
    app.run(debug=True, host=SERVER_HOST, port=SERVER_PORT)