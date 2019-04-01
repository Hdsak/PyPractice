#9-1. Ресторан: создайте класс с именем Restaurant. 
# Метод __init__() класса Restaurant должен содержать два атрибута: restaurant_name и cuisine_type. 
# Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(),
#  который выводит сообщение о том, что ресторан открыт.
#Создайте на основе своего класса экземпляр с именем restaurant.
#  Выведите два атрибута по отдельности, затем вызовите оба метода.
class restaurant():
    """Restaurant class"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("This restaurant is "+self.restaurant_name)
        print("Cuisine is "+ self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + " is open")
barviha=restaurant('Barviha','hookah')
print(barviha.restaurant_name+barviha.cuisine_type)
barviha.describe_restaurant()
barviha.open_restaurant()
#9-2. Три ресторана: начните с класса из упражнения 9-1.
#  Создайте три разных экземпляра, вызовите для каждого экземпляра метод describe_restaurant().
lounger=restaurant("Lounger",'vip')
hp=restaurant("Hookah place",'garbage')
lounger.describe_restaurant()
hp.describe_restaurant()
#9-3. Пользователи: создайте класс с именем User.
#  Создайте два атрибута first_name и last_name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя. 
# Напишите метод describe_user(), который выводит сводку с информацией о пользователе. 
# Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя.
#Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя.
class user():
    """User class"""
    def __init__(self,first_name,last_name,**user_info):
        self.first_name=first_name
        self.last_name=last_name
        self.user_info=user_info
    def describe_user(self):
        print("Name "+ self.first_name+ "\nLast name "+self.last_name)
        for k,v in self.user_info.items():
            print(k.title()+" "+str(v))
    def greet_user(self):
        print("Hey "+self.first_name)
user_1=user("Roma",'Mexanik',location='Russia',age=25)
user_1.describe_user()
user_1.greet_user()

