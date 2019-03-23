from pymongo import MongoClient
from configs.Config import MONGODR_URI

def mongo_connection():
    mongo_url = MONGODR_URI
    uranlo_client = MongoClient(mongo_url)
    return uranlo_client.get_database()
