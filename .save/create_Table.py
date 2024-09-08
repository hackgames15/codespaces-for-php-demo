import argparse
import os
    
# Setting up argparse for command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--name', help="name Table")
args = parser.parse_args()

os.makedirs(args.name, exist_ok=True)
