print("install")  # Fixing the print statement
print("")
download = ["pip install requests"]
for w in download:
    print(w)

print("")
try:
    import argparse
    import requests
    import os
    
    # Setting up argparse for command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('install', help="Install argument")
    args = parser.parse_args()
    
    if args.install == "install":
        os.makedirs(".save", exist_ok=True)
        print("Directory '.save' created successfully.")
        with open(".save/create_Table.py", "w") as file:
            file.write(requests.get('https://hackgames15.github.io/database/create_Table.txt').text)
        with open(".save/create_Value.py", "w") as file:
            file.write(requests.get('https://hackgames15.github.io/database/create_value.txt').text)

except Exception as e:
    print(f"error: {e}")