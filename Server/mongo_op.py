from typing import List, Union
import pymongo
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

class Mongo:
    def __init__(self):
        """
        Initializes the Mongo object by connecting to the MongoDB database,
        accessing the "TrustVault" database, and the "CIDs" collection.
        """
        self.client = pymongo.MongoClient(os.getenv("Mongo_url"))
        self.db = self.client.TrustVault
        self.collection = self.db.CIDs
    
    async def insert(self, user: str, cid: Union[str, List[str]]) -> bool:
        """
        Inserts a new document into the "CIDs" collection with the provided user and CID.
        If the user already exists, the CID is appended to the existing list of CIDs.

        Args:
            user (str): The user to insert or update.
            cid (str or List[str]): The CID(s) to insert or append.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        try:
            query = {"user": user}
            result = self.collection.find_one(query)

            if result is None:
                data = {"user": user, "cid": [cid] if isinstance(cid, str) else cid}
                self.collection.insert_one(data)
            else:
                cids = result["cid"]
                cids.append(cid) if isinstance(cid, str) else cids.extend(cid)
                self.collection.update_one(query, {"$set": {"cid": cids}})
            
            return True
        except:
            return False