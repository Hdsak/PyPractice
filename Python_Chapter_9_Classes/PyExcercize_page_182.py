#9-10. Импортирование класса Restaurant:
#  возьмите последнюю версию класса Restaurant 
# и сохраните ее в модуле. Создайте отдельный файл,
#  импортирующий класс Restaurant. 
# Создайте экземпляр Restaurant и вызовите 
# один из методов Restaurant, чтобы показать, 
# что команда import работает правильно.
from restaurant import restaurant
barviha=restaurant("Barviha","Hookah")
barviha.describe_restaurant()
#9-11. Импортирование класса Admin: начните с версии класса из упражнения 9-8 (с. 176).
#  Сохраните классы User, Privileges и Admin в одном модуле.
#  Создайте отдельный файл, создайте экземпляр Admin и вызовите метод show_privileges(),
#  чтобы показать, что все работает правильно.
from users_for_excercize import Admin,user,Privileges
My_Admin=Admin("Roma","Mexanik",22)
My_Admin.describe_user()
My_Admin.privileges.show_privileges()

#9-12. Множественные модули: сохраните класс User в одном модуле,
#  а классы Privileges и Admin в другом модуле.
#  В отдельном файле создайте экземпляр Admin и вызовите метод show_privileges(),
#  чтобы показать, что все работает правильно.
from admin import Admin as ad
new_ad=ad("Max","Maximov",22)
new_ad.describe_user()
new_ad.privileges.show_privileges()