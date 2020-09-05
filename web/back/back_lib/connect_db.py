from pymongo import MongoClient

def connect_mongo():
    client = MongoClient("[URL]")
    return client

