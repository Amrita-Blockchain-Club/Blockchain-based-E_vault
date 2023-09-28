from server import get_only_cid
import mongo_op as mongo

# Mongo = mongo.Mongo()

# status = Mongo.isFileExist("0x59a0Ee7fDc4Eb1A941ff8c3c6bcdF69446398D38","QmcKgv8HV4iuiBwtxwYoXC5oTN8LDkpCfdaUM4aVNNmypL")
# print(status)
# {"_id":{"$oid":"651304f3c9c461b361becdd9"},"user":"0x59a0Ee7fDc4Eb1A941ff8c3c6bcdF69446398D38","cid":["QmcKgv8HV4iuiBwtxwYoXC5oTN8LDkpCfdaUM4aVNNmypL","QmP4iPA3aDP1HpjgSmBjWGgGmvLMfajwP7492gFAqNQ4Eg"]}

puzzle = """added QmX24HY4K4cELoBUnkr9VTPKCV4oNqc3QxuJtcPYJ3RqhP server.py
 3.87 KiB / 3.87 KiB [===============================================================================================================================================================================================================] 100.00%"""

word = puzzle.split(" ")[1]
print(word)