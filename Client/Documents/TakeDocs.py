import os
import asyncio
import shutil

async def Documents_Upload(document_path: str, destination_path: str) -> bool:
    try:
        if os.path.exists(document_path):
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.copy(document_path, destination_path)
            return True
        else:
            print("The specified file does not exist.")
            return False
    except Exception as e:
        print(f"An error occurred during the file copy operation: {e}")
        return False


document_path = "/home/neeraj/Downloads/Idea-Presentation-Format-SIH2023-College.pdf"
destination_path = "Server/LocalFolder"
val = asyncio.run(Documents_Upload(document_path=document_path, destination_path=destination_path))
print(val)