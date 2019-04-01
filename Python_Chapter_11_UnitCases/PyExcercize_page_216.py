#11-1. Город, страна: напишите функцию, которая получает два параметра: 
# название страны и название города.
#  Функция должна возвращать одну строку в формате «Город, Страна»,
#  например «Santiago, Chile». Сохраните функцию в модуле с именем city_functions.py.
#Создайте файл test_cities.py для тестирования только что написанной функции 
# (не забудьте импортировать unittest и тестируемую функцию).
#  Напишите метод test_city_country() для проверки того, 
# что вызов функции с такими значениями, как ‘santiago’ и ‘chile’, дает правильную строку.
#  Запустите test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.
#11-2. Население: измените свою функцию так, чтобы у нее был третий обязательный параметр — население. 
# В новой версии функция должна возвращать одну строку вида «Santiago, Chile — population 5000000.» 
# Снова запустите программу test_cities.py.
#  Убедитесь в том, что тест test_city_country() на этот раз не проходит.
#Измените функцию так, чтобы параметр населения стал необязательным.
#  Снова запустите test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.
#Напишите второй тест test_city_country_population(), 
# который проверяет вызов функции со значениями ‘santiago’, ‘chile’ и ‘population=5000000’.
#  Снова запустите test_cities.py и убедитесь в том, что новый тест проходит успешно.

from city_functions import city
from city_functions import city_task_2
import unittest
class UnitTestFunc(unittest.TestCase):
    def test_countr_name(self):
        place_name=city("santiago","chile")
        self.assertEqual(place_name,"Santiago, Chile")
    def test_task_2(self):
        pop_with_place=city_task_2("santiago","chile",500000)   
        self.assertEqual(pop_with_place,"Santiago, Chile 500000")
unittest.main()
