import argparse
from commands.add import add_expense
from commands.list import list_expenses
from commands.summarize import summarize_expenses
from commands.update import update_expense
from commands.delete import delete_expense

def main():
    """
    Main function to set up the command-line interface and handle user commands.
    """
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Adding command handler
    add_parser = subparsers.add_parser('add', help="Add a new Expense")
    add_parser.add_argument('--description', required=True,type=str, help="Expense Description")
    add_parser.add_argument('--amount', required=True, type=float , help="Expense Amount")
    add_parser.set_defaults(func=add_expense)

    # List command handler
    list_parser = subparsers.add_parser('list', help="List All Expenses")
    list_parser.set_defaults(func=list_expenses)

    # Summarizing command handler
    summary_parser = subparsers.add_parser('summary', help="Summarize Expenses")
    summary_parser.add_argument('--month', type=int, choices=range(1,13), help="Number of the Month")
    summary_parser.set_defaults(func=summarize_expenses)

    # Updating command handler
    update_parser = subparsers.add_parser('update', help="Update an Expense")
    update_parser.add_argument('--id', type=int, required=True, help="Expense Number to Update")
    update_parser.add_argument('--description',type=str, help="Expense Description")
    update_parser.add_argument('--amount', type=float , help="Expense Amount")
    update_parser.set_defaults(func=update_expense)

    # Delete command handler
    delete_parser = subparsers.add_parser('delete', help="Delete an Expense")
    delete_parser.add_argument('--id', type=int, required=True, help="Expense Number to Delete")
    delete_parser.set_defaults(func=delete_expense)

    # Parse arguments and call the appropriate function
    args = parser.parse_args()
    args.func(args)

    

if __name__ == "__main__":
    main()