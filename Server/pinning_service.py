import mongo_op as mongo
import asyncio
import time
import Run_commands as run
Mongo = mongo.Mongo()


async def heart_beat(status, cid):
    if not status:
        result = await run.run_ipfs_command(f"ipfs pin add {cid}")
        if result is None:
            print(f"[-] An error occurred while pinning the file. CID: {cid}")
        else:
            print(f"[+] File pinned. CID: {cid}")
    else:
        print(f"[+] File pinned. CID: {cid}")


async def Pinning_service(CID) -> bool:
    for cid in range(CID):
        command = f"ipfs pin add {cid}"
        result = await run.run_ipfs_command(command)
        if result is None:
            print(f"[-] Trying again to pin the file. CID: {cid}")
            await heart_beat(False, cid)
        else:
            await heart_beat(True, cid)
    return True


async def main():
    documents = await Mongo.read()
    
    status = await Pinning_service(documents)

    if status:
        print("[+] All files pinned successfully.")
        time.sleep(8)
    else:
        print("[-] An error occurred while pinning the files.")
        time.sleep(8)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())