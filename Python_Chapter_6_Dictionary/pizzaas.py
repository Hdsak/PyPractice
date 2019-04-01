pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']}
print("You have ordered " + pizza['crust'] + '-crust pizza ' + "with following toppings: ")
for n in pizza['toppings']:
    print("\t"+n.title())

