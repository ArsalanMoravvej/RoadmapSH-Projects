from .db import expenses_collection, get_new_id
from datetime import datetime, timezone

def add_expense(args):
    expense = {
        "_id": get_new_id(),
        "description": args.description,
        "amount":      args.amount,
        "createdAt": datetime.now(timezone.utc),
        "modifiedAt": None,   
        "isDeleted": False
    }

    result = expenses_collection.insert_one(expense)
    
    if result.acknowledged:
        print(f"Expense added successfully! ID: {result.inserted_id}")
    else:
        print("Error: Expense could not be added.")