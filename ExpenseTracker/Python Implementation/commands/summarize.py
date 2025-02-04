from .db import expenses_collection

def summarize_expenses(args):
    filters = {"isDeleted": False}

    if args.month:
        filters["$expr"] = {"$eq": [{ "$month": "$createdAt" }, args.month]}

    pipeline = [
        {"$match": filters},
        {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
    ]

    result = list(expenses_collection.aggregate(pipeline))

    if not result:
        print("No expenses found.")
    else:
        print(f"Total Expenses: ${result[0]['total']:.2f}")
