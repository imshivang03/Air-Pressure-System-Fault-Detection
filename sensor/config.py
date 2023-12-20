import pandas as pd
import pymongo
import json
from dataclasses import dataclass
import os

#Provide the mongodb localhost url to connect python to mongodb.
@dataclass
class EnvironmentVariable:
    mongo_db_url: os.getenv("MONGO_DB_URL")

client= pymongo.MongoClient()
