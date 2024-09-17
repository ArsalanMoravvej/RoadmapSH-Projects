#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple CLI that responds with a message.")
    parser.add_argument("name", help="Your name")
    args = parser.parse_args()
    
    print(f"Hello, {args.name}! This is a simple CLI response.")

if __name__ == "__main__":
    main()