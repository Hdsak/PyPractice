#5-3.  Цвета 1: представьте, что в вашей компьютерной игре только что был
#подбит корабль пришельцев.  Создайте переменную с именем alien_color и
#присвойте ей значение ‘green’, ‘yellow’ или ‘red’.
#Напишите команду if для проверки того, что переменная содержит значение
#‘green’.  Если условие истинно, выведите сообщение о том, что игрок только что
#заработал 5 очков.
#Напишите одну версию программы, в которой условие if выполняется, и другую
#версию, в которой оно не выполняется.  (Во второй версии никакое сообщение
#выводиться не должно.)
alien_color = 'green'
if alien_color == 'green':
    print("You've earned 5 points")
alien_color = 'red'
if alien_color == 'green':
    print("You've earned 5 points")
#5-4.  Цвета 2: выберите цвет, как это было сделано в упражнении 5-3, и
#напишите цепочку if-else.
#Напишите команду if для проверки того, что переменная содержит значение
#‘green’.  Если условие истинно, выведите сообщение о том, что игрок только что
#заработал 5 очков.
#Если переменная содержит любое другое значение, выведите сообщение о том, что
#игрок только что заработал 10 очков.
#Напишите одну версию программы, в которой выполняется блок if, и другую
#версию, в которой выполняется блок else.
color = 'yellow'
if color == 'green':
    print("You've earned 5 points")
else:
    print("You've earned 10 points")
#5-5.  Цвета 3: преобразуйте цепочку if-else из упражнения 5-4 в цепочку
#if-elif-else.
#Если переменная содержит значение 'green’, выведите сообщение о том, что игрок
#только что заработал 5 очков.
#Если переменная содержит значение 'yellow’, выведите сообщение о том, что
#игрок только что заработал 10 очков.
#Если переменная содержит значение 'red’, выведите сообщение о том, что игрок
#только что заработал 15 очков.
#Напишите три версии программы и проследите за тем, чтобы для каждого цвета
#пришельца выводилось соответствующее сообщение.
color = 'red'
if color == 'green':
    print("You've earned 5 points")
elif color == 'yellow':
    print("You've earned 10 points")
else:
    print("15 points")

#5-6.  Периоды жизни: напишите цепочку if-elif-else для определения периода
#жизни человека.  Присвойте значение переменной age, а затем выведите
#сообщение.
#Если значение меньше 2 — младенец.
#Если значение больше или равно 2, но меньше 4 — малыш.
#Если значение больше или равно 4, но меньше 13 — ребенок.
#Если значение больше или равно 13, но меньше 20 — подросток.
#Если значение больше или равно 20, но меньше 65 — взрослый.
#Если значение больше или равно 65 — пожилой человек.
age = 115
if age < 2:
    print("Mladenec")
elif age >= 2 and age < 4:
    print("Baby")
elif age >= 4 and age < 13:
    print("Kid")
elif age >= 13 and age < 20:
    print("Podrostok")
elif age >= 20 and age < 65:
    print("Old")
else:
    print("Glad")
#5-7.  Любимый фрукт: составьте список своих любимых фруктов.  Напишите серию
#независимых команд if для проверки того, присутствуют ли некоторые фрукты в
#списке.
#Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
#Напишите пять команд if.  Каждая команда должна проверять, входит ли
#определенный тип фрукта в список.  Если фрукт входит в список, блок if должен
#выводить сообщение вида «You really like bananas!».
fruit_list = ['banana','apple','raspberry','grape']
if 'banana' in fruit_list:
    print("Bananas here")
if 'soda' not in fruit_list:
    print("Fuck you soda")
favorite_fruits = ['apple','grape','cucumber']
if 'grape' in favorite_fruits:
    print("You really like grape!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'cucumber' in favorite_fruits:
    print("You really like cucumber!")
if 'raspberry' in favorite_fruits:
    print("You really like raspberry!")
if 'gooseberry' in favorite_fruits:
    print("goosberry here")