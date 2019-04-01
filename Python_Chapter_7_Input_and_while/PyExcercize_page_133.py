#7-8.  Сэндвичи: создайте список с именем sandwich_orders, заполните его
#названиями различных видов сэндвичей.  Создайте пустой список с именем
#finished_sandwiches.  В цикле переберите элементы первого списка и выведите
#сообщение для каждого элемента (например, «I made your tuna sandwich»).  После
#этого каждый сэндвич из первого списка перемещается в список
#finished_sandwiches.  После того как все элементы первого списка будут
#обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей.
sandwich_orders=["hot-dog",'tuna','shaverma']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print("I made your a "+sandwich+" sandwich")
print("Finished sandwiches:")
for n in finished_sandwiches:

    print("\t"+n)
#7-9.  Без пастрами: используя список sandwich_orders из упражнения 7-8,
#проследите за тем, чтобы значение ‘pastrami’ встречалось в списке как минимум
#три раза.  Добавьте в начало программы код для вывода сообщения о том, что
#пастрами больше нет, и напишите цикл while для удаления всех вхождений
#‘pastrami’ из sandwich_orders.  Убедитесь в том, что в finished_sandwiches
#значение ‘pastrami’ не встречается ни одного раза.
sandwich_orders=["hot-dog",'pastrami','tuna','pastrami','shaverma','pastrami']
finished_sandwiches=[]
print("pastrami is out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich=sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print("I made your a "+sandwich+" sandwich")
print("Finished sandwiches:")
for n in finished_sandwiches:

    print("\t"+n)
#7-10.  Отпуск мечты: напишите программу, которая опрашивает пользователей, где
#бы они хотели провести отпуск.  Включите блок кода для вывода результатов
#опроса.
info={}
active=True
greetings_message="\nHi what is your name ? "
question_message="Where would you like to spent your weekend ? "
while active:
    name=input(greetings_message)
    place=input(question_message)
    info[name]=place
    stop=input("\nWould you like to stop? ")
    if stop.lower() =='yes':
        print("Thanks for the visit\n")
        active=False
for k,v in info.items():
    print(k.title() + " want to spent weekend in "+ v.title())

