import asyncio
import os

async def run_ipfs_command(command, file=False):
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if file:
            return stdout.decode().strip()
        else:
            return True
    except Exception as e:
        print(e)
        return None


async def get_only_cid(file_path: str) -> str:
    """
    Get the CID of a file without uploading it to IPFS.

    Args:
        file_path: A string representing the path to the file.

    Returns:
        A string representing the CID of the file.
    """

    command = f"ipfs add --only-hash {file_path}"
    cid =  await run_ipfs_command(command)

    if cid is None:
        print("[-] An error occurred while uploading to IPFS.")
        return None
    else:
        return cid.split(" ")[1]
    
    
    
async def upload_to_ipfs(file_path):
    """
    Upload File to the IPFS.

    Args:
        file_path: A string representing the path to the file.

    Returns:
        A string representing the CID of the file.
    """
        
    command = f"ipfs add -Q {file_path}"
    cid = await run_ipfs_command(command)

    if cid is None:
        print("[-] An error occurred while uploading to IPFS.")
        return None
    else:
        return cid


async def Check_dir(directory) -> bool:
    """
    Ensure that a directory exists.

    Args:
        directory: A string representing the path to the directory.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            return True
        else:
            return True
    except:
        return False


async def download_from_ipfs(CID, filename):
    """
    Download File from the IPFS.

    Args:
        CID: A string representing the CID of the file.

    Returns:
        A string representing the path to the file.
    """
    dir_status = await Check_dir(f"./Storage/{CID}")
    if not dir_status:
        print("[-] An error occurred while creating the directory.")
        return None
    else:
        extension = filename.split(".")[-1]
        filename = f"{CID}.{extension}"
        path = f"./Storage/{CID}/{filename}"
        command = f"ipfs get {CID} -o {path}"

        try:
            File = await run_ipfs_command(command, file=True)
        except Exception as e:
            print(e)
            return None

    if File is None:
        print("[-] An error occurred while downloading from IPFS.")
        return None
    else:
        return File

# async def main():
#     File = await download_from_ipfs("QmYaMvMeJdzMSW3hAmxgxzGLvrw5EhomfdHYBep8AYpPVg","file.go")
#     print(File)

# asyncio.run(main())