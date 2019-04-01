import json
numbers=[1,3,4,5,7,8]
filename="json_numbers.json"
with open(filename,"w") as text_file:
    json.dump(numbers,text_file)
print(numbers)