from .db import expenses_collection
from datetime import datetime, timezone

def delete_expense(args):
    """
    Deletes an expense by marking it as deleted (soft delete).
    """
    result = expenses_collection.update_one(
        {"_id": args.id},
        {"$set": {"isDeleted": True}}
    )

    if result.matched_count == 0:
        print(f"Expense with ID {args.id}, couldn't be found.")
    elif result.modified_count == 0:
        print(f"Expense with ID {args.id} was already deleted.")
    else:
        expenses_collection.update_one(
            {"_id": args.id},
            {"$set": {"modifiedAt": datetime.now(timezone.utc)}})
        print(f"Expense with ID {args.id} was deleted successfully.")