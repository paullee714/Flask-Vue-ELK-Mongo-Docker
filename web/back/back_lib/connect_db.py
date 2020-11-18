from pymongo import MongoClient

def connect_mongo():
    client = MongoClient("localhost",27017)
    return client
