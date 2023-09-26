import socket
import tqdm
import os
import sys

def sendfile(public_key: str, filepath: str) -> bool:
    """
    Send a file over a network using a client-server model.

    Args:
        public_key: A string representing the public key used for encryption.
        filename: A string representing the name of the file to be sent.

    Returns:
        None
    """

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    Filename = filepath.split("/")
    Filename = Filename[-1]


    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    host = "192.168.101.50"
    port = 5100

    filesize = os.path.getsize(filepath)
    try:
        with socket.socket() as s:
            print(f"[+] Connecting to {host}:{port}")
            s.connect((host, port))
            print("[+] Connected.")

            message = f"{Filename}{SEPARATOR}{filesize}{SEPARATOR}{public_key}".encode()
            s.send(message)

            progress = tqdm.tqdm(range(filesize), f"Sending {Filename}", unit="B", unit_scale=True, unit_divisor=1024)
            with open(filepath, "rb") as f:
                while True:
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    s.sendall(bytes_read)
                    progress.update(len(bytes_read))

            return True
    except:
        return False


if __name__ == "__main__":
    status = sendfile(filepath="/home/neeraj/Documents/NoCode+CodeBase_Tuning.pdf", public_key="0x59a0Ee7fDc4Eb1A941ff8c3c6bcdF69446398D38")
    
    if status:
        print("[+] File sent successfully.")
    else:
        print("[-] An error occurred while sending the file.")
