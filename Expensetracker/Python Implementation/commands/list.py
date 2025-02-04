from .db import expenses_collection
from prettytable import prettytable

def list_expenses(args):
    expenses = expenses_collection.find({"isDeleted": False})

    print(list(expenses))