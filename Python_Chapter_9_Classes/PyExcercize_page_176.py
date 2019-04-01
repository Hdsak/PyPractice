#9-6. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. 
# Напишите класс IceCreamStand, наследующий от класса Restaurant из упражнения 9-1 (с. 165) или упражнения 9-4 (с. 169).
#  Подойдет любая версия класса; просто выберите ту, которая вам больше нравится.
#  Добавьте атрибут с именем flavors для хранения списка сортов мороженого. 
# Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand и вызовите этот метод.
class restaurant():
    """Restaurant class"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("This restaurant is "+str(self.restaurant_name))
        print("Cuisine is "+ self.cuisine_type)
    def open_restaurant(self):
        print(str(self.restaurant_name) + " is open")
class IceCreamStand(restaurant):
    """IceCreamStand"""
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        """Constructor"""
        super().__init__(restaurant,cuisine_type)
        self.flavors=flavors
    def print_IceCream(self):
        print("Ice cream involved")
        for n in self.flavors:
            print(n)
flavors=["Karkade","Berry","Cranberry"]
Baskin_Robins=IceCreamStand("Baskin_Robins","Ice_creamStand",flavors)
Baskin_Robins.print_IceCream()
#9-7. Администратор: администратор — особая разновидность пользователя.
#  Напишите класс с именем Admin, наследующий от класса User из упражнения 9-3 (с. 165) или упражнения 9-5 (с. 170).
#  Добавьте атрибут privileges для хранения списка строк вида «разрешено добавлять сообщения»,
#  «разрешено удалять пользователей», «разрешено банить пользователей» и т. д. 
# Напишите метод show_privileges() для вывода набора привилегий администратора. 
# Создайте экземпляр Admin и вызовите свой метод.
#9-8. Привилегии: напишите класс Privileges. 
# Класс должен содержать всего один атрибут privileges со списком строк из упражнения 9-7.
#  Переместите метод show_privileges() в этот класс. 
# Создайте экземпляр Privileges как атрибут класса Admin. 
# Создайте новый экземпляр Admin и используйте свой метод для вывода списка привилегий.
class Privileges():
    def __init__(self):
        self.privileges=["разрешено добавлять сообщения","разрешено удалять пользователей", "разрешено банить пользователей"]
    def show_privileges(self):
        for n in self.privileges:
            print(n)
class user():
    """User class"""
    def __init__(self,first_name,last_name,user_info):
        self.first_name=first_name
        self.last_name=last_name
        self.user_info=user_info
    def describe_user(self):
        print("Name "+ self.first_name+ "\nLast name "+self.last_name)
        # for k,v in self.user_info.items():
        #     print(k.title()+" "+str(v))
    def greet_user(self):
        print("Hey "+self.first_name)
class Admin(user):
    def __init__(self,first_name,last_name,user_info):
        super().__init__(first_name,last_name,user_info)
        self.privileges=Privileges()    
dic={'loc':'RU','Ls':"cake"}
user_1=Admin("Roma",'Mexanik',24)
user_1.describe_user()
user_1.privileges.show_privileges()
#9-9. Обновление аккумулятора: используйте окончательную версию программы electric_car.py из этого раздела.
#  Добавьте в класс Battery метод с именем upgrade_battery().
#  Этот метод должен проверять размер аккумулятора и устанавливать мощность равной 85, если она имеет другое значение.
#  Создайте экземпляр электромобиля с аккумулятором по умолчанию, вызовите get_range(),
#  а затем вызовите get_range() во второй раз после вызова upgrade_battery(). 
# Убедитесь в том, что запас хода увеличился.
class car():
    """Simple  car class"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """Return best formatted name"""
        long_name=str(self.model).title()+" "+str(self.year).title()+" "+str(self.make).title()
        return long_name
    def odometer_update(self,value):
        self.odometer_reading=value
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")
class battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def upgrade_battery(self):
        if self.battery_size!=85:
            self.battery_size=85
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=265
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
class electric_car(car):
    def __init__(self,make,model,year):
        """Constructor for electric car"""
        super().__init__(make,model,year)
        self.battery_size=battery()
my_electric_car=electric_car("AUdi",'a4',2016)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery_size.describe_battery()
my_electric_car.battery_size.get_range()
my_electric_car.battery_size.upgrade_battery()
my_electric_car.battery_size.get_range()