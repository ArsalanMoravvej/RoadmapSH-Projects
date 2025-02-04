from .db import expenses_collection
from prettytable import PrettyTable

def list_expenses(args):
    expenses = list(expenses_collection.find({"isDeleted": False}))

    if not expenses:
        print("No expenses found.")
        return

    table = PrettyTable(["ID", "Date", "Description", "Amount"])
    table.border = False

    for expense in expenses:
        table.add_row([
            expense.get("_id", "N/A"),
            expense["createdAt"].date(),
            expense["description"],
            "$" + str(expense["amount"])
        ])
    
    print(table)