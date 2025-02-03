import argparse

def update_expense(args):
    if args.description is None and args.amount is None:
        raise argparse.ArgumentTypeError("At least one of --description or --amount must be provided.")
    print(args)
