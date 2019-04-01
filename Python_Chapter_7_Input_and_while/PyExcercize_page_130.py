#7-4.  Дополнения для пиццы: напишите цикл, который предлагает пользователю
#вводить дополнения для пиццы до тех пор, пока не будет введено значение
#'quit’.  При вводе каждого дополнения выведите сообщение о том, что это
#дополнение включено в заказ.
toppings="Please input wanted toppings : "
toppings_list=[]
while True:
    prompt=input(toppings)
    if prompt=='quit':
        break
    else:
        print(prompt+" added.")
        toppings_list.append(prompt)
print("your order:")
print(toppings_list)

#7-5.  Билеты в кино: кинотеатр установил несколько вариантов цены на билеты в
#зависимости от возраста посетителя.  Для посетителей младше 3 лет билет
#бесплатный; в возрасте от 3 до 12 билет стоит $10; наконец, если возраст
#посетителя больше 12, билет стоит $15.  Напишите цикл, который предлагает
#пользователю ввести возраст и выводит цену билета.
active=True
while active:
    age=input("Input your age : ")
    if int(age)<3:
        print("Feel free your age is : " + age)
    elif int(age)<12:
        print("$10 your age is : " + age)
    else:
        print("$15 your age is : " + age)
