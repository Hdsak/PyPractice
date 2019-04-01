#11-3. Работник: напишите класс Employee,  представляющий работника.
#  Метод __init__() должен получать имя, фамилию и ежегодный оклад;
#  все эти значения должны сохраняться в атрибутах. 
# Напишите метод give_raise(), который по умолчанию увеличивает ежегодный оклад на $5000 
# — но при этом может получать другую величину прибавки.
#Напишите тестовый сценарий для Employee.
#  Напишите два тестовых метода, test_give_default_raise() и test_give_custom_raise().
#  Используйте метод setUp(), чтобы вам не приходилось заново создавать 
# экземпляр Employee в каждом тестовом методе. 
# Запустите свой тестовый сценарий и убедитесь в том, что оба теста прошли успешно.
import unittest
from Employee_class import Employee
class task_1_test(unittest.TestCase):
    def setUp(self):
        self.me=Employee("Roma","Mexan",20000)       
    def test_employee(self): 
        self.me.give_raise()      
        self.assertEqual(25000,self.me.salary)
    def test_give_custom_raise(self):
        self.me.give_raise(10000)
        self.assertEqual(30000,self.me.salary)
unittest.main()
