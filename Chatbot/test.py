import json

# Open and load JSON file
jsonFile = "Chatbot\data.json"

with open(jsonFile, "r") as file:
    data = json.load(file)

print(data)           # prints it as a Python dict
print(data["name"])   # access a value by key