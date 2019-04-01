import json
filename="user.json"
try:
    with open(filename) as user_greet:
        name=json.load(user_greet)
        print("Hi "+name)
except FileNotFoundError:
    with open(filename,"w") as save_name:
        name=input("Please enter your name i'll remember you ")
        json.dump(name,save_name)
