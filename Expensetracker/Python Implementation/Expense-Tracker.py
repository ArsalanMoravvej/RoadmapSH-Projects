import argparse

def add_expense(args):
    print(args)

def summarize_expenses(args):
    print(args)

def main():
    """
    Main function to set up the command-line interface and handle user commands.
    """
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    #Adding command handler
    add_parser = subparsers.add_parser('add', help="Add a new Expense")
    add_parser.add_argument('--description', required=True,type=str, help="Expense Description")
    add_parser.add_argument('--amount', required=True, type=float , help="Expense Amount")
    add_parser.set_defaults(func=add_expense)

    #Summarizing command handler
    summary_parser = subparsers.add_parser('summary', help="Summarize Expenses")
    summary_parser.add_argument('--month', type=int, help="Summarize By Month Number")
    summary_parser.set_defaults(func=summarize_expenses)


    # Parse arguments and call the appropriate function
    args = parser.parse_args()
    args.func(args)

    

if __name__ == "__main__":
    main()