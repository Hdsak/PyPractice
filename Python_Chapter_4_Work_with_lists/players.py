players=['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:5])
print("Here the first three players in the team")
for val in players[:3]:
    print(val)
friends_foods=['pizza', 'falafel', 'carrot cake']
my_foods=friends_foods[:]
my_foods.append("Milk")
my_foods.append("Ice")
friends_foods.append("Cock")
friends_foods.append("Ice")
print("My fav food is ")
print(my_foods)
print("My friends food ")
print(friends_foods)
print("This is first three items in list")
print(my_foods[:3])
print("This is middle three items in list")
print(my_foods[1:-1])
print("This is last three items in list")
print(my_foods[2:])