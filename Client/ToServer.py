import socket
import tqdm
import os
import sys

def sendfile(public_key: str, filename: str) -> None:
    """
    Send a file over a network using a client-server model.

    Args:
        public_key: A string representing the public key used for encryption.
        filename: A string representing the name of the file to be sent.

    Returns:
        None
    """
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    host = "127.0.0.1"
    port = 5100

    filesize = os.path.getsize(filename)

    with socket.socket() as s:
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected.")

        message = f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{public_key}".encode()
        s.send(message)

        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                progress.update(len(bytes_read))

        print("[+] File sent successfully.")

# End of improved code


if __name__ == "__main__":
    sendfile(Filename="/home/neeraj/Downloads/Idea-Presentation-Format-SIH2023-College.pdf", PublicKey="0x59a0Ee7fDc4Eb1A941ff8c3c6bcdF69446398D38")