import pymongo
from keys.py import mongo_pw, mongo_db


client = pymongo.MongoClient(f"mongodb+srv://darius759:{mongo_pw}@cluster0.klg5k.mongodb.net/{mongo_db}?retryWrites=true&w=majority")
db = client.test

