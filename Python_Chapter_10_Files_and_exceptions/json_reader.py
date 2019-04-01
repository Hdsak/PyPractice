import json
filename="json_numbers.json"
with open(filename) as json_numbers:
    numbers=json.load(json_numbers)
print(numbers)