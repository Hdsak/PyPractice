#9-4. Посетители: начните с программы из упражнения 9-1 (с. 165).
#  Добавьте атрибут number_served со значением по умолчанию 0;
#  он представляет количество обслуженных посетителей.
#  Создайте экземпляр с именем restaurant.
#  Выведите значение number_served, потом измените и выведите снова.
#Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных посетителей.
#  Вызовите метод с новым числом, снова выведите значение.
#Добавьте метод с именем increment_number_served(), который увеличивает количество обслуженных посетителей на заданную величину.
#  Вызовите этот метод с любым числом, которое могло бы представлять количество обслуженных клиентов — скажем, за один день.
class restaurant():
    """Restaurant class"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def set_number_served(self,number):
        self.number_served=number
    def increment_number_served(self,number):
        self.number_served+=number
    def describe_restaurant(self):
        print("This restaurant is "+self.restaurant_name)
        print("Cuisine is "+ self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + " is open")
barviha=restaurant("Barviha",'hookah')
print(barviha.number_served)
barviha.set_number_served(24)
print(barviha.number_served)
barviha.increment_number_served(6)
print(barviha.number_served)
#9-5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9-3 (с. 165).
#  Напишите метод increment_login_attempts(), увеличивающий значение login_attempts на 1.
#  Напишите другой метод с именем reset_login_attempts(), обнуляющий значение login_attempts.
#Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз.
#  Выведите значение login_attempts, чтобы убедиться в том, что значение было изменено правильно, а затем вызовите reset_login_attempts().
#  Снова выведите login_attempts и убедитесь в том, что значение обнулилось.
class user():
    """User class"""
    def __init__(self,first_name,last_name,**user_info):
        self.first_name=first_name
        self.last_name=last_name
        self.user_info=user_info
        self.login_attempts=0
    def increment_login_attempts(self):
        self.login_attempts=self.login_attempts+1
    def reset_login_attempts(self):
        self.login_attempts=0    
    def describe_user(self):
        print("Name "+ self.first_name+ "\nLast name "+self.last_name)
        for k,v in self.user_info.items():
            print(k.title()+" "+str(v))
    def greet_user(self):
        print("Hey "+self.first_name)
user_1=user("Roma",'Mexanik',location='Russia',age=25)
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)