import argparse
import os

# Setting up argparse for command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--name_table', help="Name of the directory", required=True)
parser.add_argument('--name_value', help="Name of the value/file", required=True)
parser.add_argument('--data', help="Data to write to the file", required=False)
args = parser.parse_args()

try:
    # Write the data to the file
    with open(f"{args.name_table}/{args.name_value}.txt", "w") as file:
        if args.data is not None:
            file.write(args.data)
        else:
            raise ValueError("No data provided")

except Exception as e:
    # In case of error, prompt for user input
    with open(f"{args.name_table}/{args.name_value}.txt", "w") as file:
        file.write(input("text or number to save> "))