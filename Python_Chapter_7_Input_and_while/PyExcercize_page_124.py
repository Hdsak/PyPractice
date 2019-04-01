#7-1.  Прокат машин: напишите программу, которая спрашивает у пользователя,
#какую машину он хотел бы взять напрокат.  Выведите сообщение с введенными
#данными (например, “Let me see if I can find you a Subaru”).
car=input("Which car do you like to take ")
print("Let me see if i can find you a " + car)
#7-2.  Заказ стола: напишите программу, которая спрашивает у пользователя, на
#сколько мест он хочет забронировать стол в ресторане.  Если введенное число
#больше 8, выведите сообщение о том, что пользователю придется подождать.  В
#противном случае сообщите, что стол готов.
booking=input("How much places you wanna take : ")
if int(booking)>8:
    print("Wait mthfcr")
else:
    print("Table is done")

#7-3.  Числа, кратные 10: запросите у пользователя число и сообщите, кратно оно
#10 или нет.
number=input("Input a number : ")
if int(number) % 10 ==0:
    print(number + " is kraten 10")
else:
    print(number + " is dont kraten 10")