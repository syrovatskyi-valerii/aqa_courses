import json
import os

def check_valid_json(filename):
    try:
        with open(filename, 'r') as file:
            json.load(file)
            print(f" File '{filename}' is VALID JSON.")
        return True
    except json.JSONDecodeError as e:
        print(f" File '{filename}' IS NOT VALID JSON:", e)
        return False
    except Exception as e:
        print("Error reading file:", e)
        return False

# find all json file in current dir
current_directory = os.getcwd()
files_in_directory = os.listdir(current_directory)
json_files = [file for file in files_in_directory if file.endswith('.json')]

# check each json files in current dir
for filename in json_files:
    check_valid_json(filename)