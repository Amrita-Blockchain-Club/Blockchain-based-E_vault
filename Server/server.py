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

mongo = mongo.Mongo()


async def handle_client(client_socket):
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize, PublicKey = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    directory = f"Storage/{PublicKey}"
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filepath, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
    f.close()

    # Check the mongodb for the existance of the file
    cid = await get_only_cid(filepath)

    status = mongo.isFileExist(user=PublicKey, cid=cid)

    if status:
        print(f"[/] File already exists. CID: {cid}")
       
    else:
        cid = await upload_to_ipfs(filepath)
        print(f"[+] File uploaded to IPFS. CID: {cid}")

        # update mongodb
        result = await mongo.insert(user=PublicKey, cid=cid)

        if result:
            print("[+] MongoDB database updated successfully.")
        else:
            print("[-] An error occurred while updating the MongoDB database.")

        path = os.path.join(directory, filename)
        os.remove(path)
        print(f"[+] File deleted from server. Filename: {filename}")

    # Send response to the client
    try:
        response = f"{cid}{SEPARATOR}{status}"
        client_socket.sendall(response.encode())
        print("[+] Response sent to the client.",{response})
    except:
        print("[-] An error occurred while sending the response to the client.")
    client_socket.close()


async def start_server():
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(10)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, address = await loop.run_in_executor(None, s.accept)
        print(f"[+] {address} is connected.")

        asyncio.create_task(handle_client(client_socket))

    s.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())