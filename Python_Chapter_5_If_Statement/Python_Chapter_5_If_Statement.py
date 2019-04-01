cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.capitalize())
request='mushrooms'
if request!='anchovies':
    print("Take this shit")
answer=17
if answer!=42:
    print("WRONG")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
banned_users = ['andrew', 'carolina', 'david']
#Для посетителей младше 4 лет вход бесплатный. 
#Для посетителей от 4 до 18 лет билет стоит $5. 
#Для посетителей от 18 лет и старше билет стоит $10.
age=12
if age<4:
    print("free")
elif (age>4 and age<18):
    print('5$')
else:
    print('10$')
