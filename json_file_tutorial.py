import json

# open and read json file
with open('states.json','r') as file:
    data=json.load(file)
print(data)