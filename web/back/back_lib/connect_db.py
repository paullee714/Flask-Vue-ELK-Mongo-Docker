from pymongo import MongoClient

def connect_mongo():
    client = MongoClient("mongodb+srv://ba93love:qkdnf93@secret-flask.4yljd.gcp.mongodb.net/wool-secret-tweeter?retryWrites=true&w=majority")
    return client

