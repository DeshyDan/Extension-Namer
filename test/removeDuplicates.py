import json

# Read the JSON file
with open("extensionNamer/extensionNames.json", 'r') as file:
    data = json.load(file)

# Create a set to store unique values
unique_values = set()

# Iterate over the JSON data
for value in data.values():
    unique_values.add(value)

# Create a new dictionary with unique values
unique_data = {key: value for key, value in data.items() if value in unique_values}

# Write the unique data to a new JSON file
with open("extensionNamer/extensionNames.json", 'w') as file:
    json.dump(unique_data, file, indent=4)
