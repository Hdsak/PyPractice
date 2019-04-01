bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1].upper())
print(bicycles[-3].capitalize())
message = "Hi do you have " + bicycles[-3].title() + " model"
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[-3]="ducati"
print(motorcycles)
motorcycles.append("Honda")
print(motorcycles)
motorcycles.insert(0,"First item in list insert")
print(motorcycles)
del motorcycles[0]
print(motorcycles)
popped_moto=motorcycles.pop()
print(popped_moto)
popped_moto=motorcycles.pop(2)
print(popped_moto)
