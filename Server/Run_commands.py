import asyncio

async def run_ipfs_command(command):
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return stdout.decode().strip()
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