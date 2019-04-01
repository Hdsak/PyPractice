#8-12. Сэндвичи: напишите функцию, которая получает список компонентов сэндвича. 
# Функция должна иметь один параметр для любого количества значений, переданных при вызове функции, 
# и выводить описание заказанного сэндвича. Вызовите функцию три раза с разными количествами аргументов.
def sandwich(*components):
    print("Sandwich components: ")
    for i in components:
        print('\t'+i)
sandwich("Cheese")
sandwich('Potato','Cheese')
sandwich('Letuce','mayo','Ketchup')
#8-13. Профиль: начните с копии программы user_profile.py. 
#  Создайте собственный профиль вызовом build_profile(), укажите имя,
#  фамилию и три другие пары «ключ—значение» для вашего описания.
def build_profile(first,last,**user_info):
    profile={}
    profile['first name']=first
    profile['last name']=last
    for k,v in user_info.items():
        profile[k]=v
    return profile
max=build_profile('Max','Maximov',classroom='5',best_game='Garrys mod',language='RU')
for k,v in max.items():
    print(k.title()+" "+v.title())
#8-14. Автомобили: напишите функцию для сохранения информации об автомобиле в словаре.
# Функция всегда должна возвращать производителя и название модели, 
# но при этом она может получать произвольное количество именованных аргументов. 
# Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация). 
# Ваша функция должна работать для вызовов следующего вида:
# car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
# Выведите возвращаемый словарь и убедитесь в том, что вся информация была сохранена правильно.
def make_car(devs,name_model,**auto_info):
    car={}
    car['car']=devs
    car['name_model']=name_model
    for k,v in auto_info.items():
        car[k]=v
    return car
porshe=make_car('porshe','911',doors='2',tow_package='True')
for k,v in porshe.items():
    print(k.title()+" "+v.title())