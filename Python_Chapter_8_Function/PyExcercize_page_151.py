#8-9. Фокусники: создайте список с именами фокусников.
#  Передайте список функции show_magicians(), которая выводит имя каждого фокусника в списке.
def show_magicians(magicians):
    for n in magicians:
        print("Name " + n.title())
#8-10. Великие фокусники: начните с копии вашей программы из упражнения 8-9. 
# Напишите функцию make_great(), которая изменяет список фокусников, добавляя к имени каждого фокусника приставку «Great».
#  Вызовите функцию show_magicians() и убедитесь в том, что список был успешно изменен.
def make_great(magicians):
    for i in range(len(magicians)):
        great_list.append(magicians[i]+" Great")
magicians=['Gendalf','Arthur','Lidia']
great_list=[]
make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_list)
#8-11. Фокусники без изменений: начните с программы из упражнения 8-10.
#  Вызовите функцию make_great() и передайте ей копию списка имен фокусников. 
# Поскольку исходный список остался неизменным, верните новый список и сохраните его в отдельном списке. 
# Вызовите функцию show_magicians() с каждым списком, чтобы показать,
#  что в одном списке остались исходные имена, 
# а в другом к имени каждого фокусника добавилась приставка «Great».