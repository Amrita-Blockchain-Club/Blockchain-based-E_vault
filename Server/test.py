from server import get_only_cid
import asyncio
async def main():
    cid = await get_only_cid(file_path="Server/NoCode+CodeBase_Tuning.pdf")
    print(cid)

asyncio.run(main())
