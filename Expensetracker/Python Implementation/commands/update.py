from .db import expenses_collection
from datetime import datetime, timezone
import argparse

def update_expense(args):
    if args.description is None and args.amount is None:
        raise argparse.ArgumentTypeError("At least one of --description or --amount must be provided.")
    
    # Build the update query dynamically
    update_data = {}
    if args.description:
        update_data["description"] = args.description
    if args.amount:
        update_data["amount"] = args.amount

    # Perform the update
    result = expenses_collection.update_one(
        {"_id": args.id, "isDeleted": False},  # Ensure the expense exists and is not deleted
        {"$set": update_data}
    )

    # Check if the update was successful
    if result.matched_count == 0:
        print(f"No expense found with ID {args.id}.")
    elif result.modified_count == 0:
        print(f"Expense with ID {args.id} already has the same values. No update performed.")
    else:
        expenses_collection.update_one(
            {"_id": args.id},
            {"$set": {"modifiedAt": datetime.now(timezone.utc)}})
        print(f"Expense with ID {args.id} updated successfully.")