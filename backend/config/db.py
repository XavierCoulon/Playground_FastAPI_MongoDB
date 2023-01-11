import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
cluster = os.environ.get("CLUSTER")

cluster = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority"
client = MongoClient(cluster)
db = client.python

