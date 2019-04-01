#4-1
pizzas_fav=["Havai","Amazon","Rumble"]
for pizza in pizzas_fav:
    print("I like "+pizza.title()+" pizza")
print("I really love pizza")
#4-2
animals=["Dog","Cat","Bob"]
for animal in animals:
    print(animal.title()+" good boy")
print("Animals are good")
#4-11
friend_pizza=pizzas_fav[:]
pizzas_fav.append("Goro")
friend_pizza.append("Lu")
print("My fav pizzas are:")
for val in pizzas_fav:
    print(val)
print("My friends like")
for val in friend_pizza:
    print(val)