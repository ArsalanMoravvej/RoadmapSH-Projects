from .db import expenses_collection
from prettytable import PrettyTable

def list_expenses(args):
    expenses = expenses_collection.find({"isDeleted": False})

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