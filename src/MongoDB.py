from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['
ShopLocal-Assistant']

# Define MongoDB collections, e.g., businesses, orders, chat_logs.
businesses = db['businesses']
orders = db['orders']
chat_logs = db['chat_logs']
