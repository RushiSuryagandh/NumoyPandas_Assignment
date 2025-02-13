# Load config files
import json
"""
    fetch the json file 
"""
def load_json():
    with open('./config.json', 'r') as file:
        data = json.load(file)
    return data