from app.config.config import Config
from pymongo import MongoClient

client = MongoClient(Config.MONGO_URI)
db = client["easyAid"]