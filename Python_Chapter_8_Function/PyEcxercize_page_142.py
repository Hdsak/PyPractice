#8-3. Футболка: напишите функцию make_shirt(), которая получает размер футболки и текст, который должен быть напечатан на ней.
#  Функция должна выводить сообщение с размером и текстом. Вызовите функцию с использованием позиционных аргументов. 
# Вызовите функцию во второй раз с использованием именованных аргументов.
def make_shirt(shirt_size,text):
    print("Your t shirt size "+str(shirt_size))
    print("Your text " + text)
make_shirt(43,'I love python')
make_shirt(text='I love c#',shirt_size=42)
#8-4. Большие футболки: измените функцию make_shirt(), чтобы футболки по умолчанию имели размер L, и на них выводился текст «I love Python.». 
# Создайте футболку с размером L и текстом по умолчанию, а также футболку любого размера с другим текстом.
def make_shirt(shirt_size='L',text="i love Python"):
    print("\nYour t shirt size "+str(shirt_size))
    print("Your text " + text)
make_shirt()
#8-5. Города: напишите функцию describe_city(), которая получает названия города и страны. 
# Функция должна выводить простое сообщение (например, «Reykjavik is in Iceland»). 
# Задайте параметру страны значение по умолчанию.
#  Вызовите свою функцию для трех разных городов, по крайней мере один из которых не находится в стране по умолчанию.
def describe_city(city_name='Rekjavik',country="iceland"):
    print(city_name+" is in "+country)
describe_city()
describe_city(country='Russia',city_name="Moscow")
describe_city('NY','Usa')
