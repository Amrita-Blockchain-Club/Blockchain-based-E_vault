import socket
import tqdm
import os
import threading
import sys
import asyncio
import mongo_op as mongo
import Run_commands as run
# small test
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5100
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
mongo = mongo.Mongo()

# async def run_ipfs_command(command):
#     process = await asyncio.create_subprocess_shell(
#         command,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE
#     )
#     stdout, stderr = await process.communicate()
#     return stdout.decode().strip()

async def upload_to_ipfs(file_path):
    command = f"ipfs add -Q {file_path}"
    cid = await run.run_ipfs_command(command)

    if cid is None:
        print("An error occurred while uploading to IPFS.")
        return None
    else:
        return cid

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

    client_socket.close()

    cid = await upload_to_ipfs(filepath)
    print(f"File uploaded to IPFS. CID: {cid}")

    # Update the MongoDB database with the CID and filename
    result = await mongo.insert(user=PublicKey, cid=cid)

    if result:
        print("MongoDB database updated successfully.")
    else:
        print("An error occurred while updating the MongoDB database.")

    path = os.path.join(directory, filename)
    os.remove(path)
    print(f"File deleted from server. Filename: {filename}")

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

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server())