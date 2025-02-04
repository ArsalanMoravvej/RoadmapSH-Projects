from pymongo import MongoClient

# Modify connection string if needed
client = MongoClient("mongodb://localhost:27017/")
db = client.expense_tracker
expenses_collection = db.expenses

def get_last_id(expenses_collection = expenses_collection):
    highest_expense = expenses_collection.find_one(sort=[("_id", -1)])
    return highest_expense["_id"] if highest_expense else 0

def get_new_id():
    return get_last_id() + 1
