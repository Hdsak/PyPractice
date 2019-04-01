#5-8.  Hello Admin: создайте список из пяти и более имен пользователей,
#включающий имя ‘admin’.  Представьте, что вы пишете код, который выводит
#приветственное сообщение для каждого пользователя после его входа на сайт.
#Переберите элементы списка и выведите сообщение для каждого пользователя.
#Для пользователя с именем 'admin’ выведите особое сообщение — например: «Hello
#admin, would you like to see a status report?»
#В остальных случаях выводите универсальное приветствие — например: «Hello
#Eric, thank you for logging in again».
user_name_list = ["admin","alpha", "omega", "beta", "teta"]

for name in user_name_list:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(name + " thank you for logging in again")
 
#5-9.  Без пользователей: добавьте в hello_admin.py команду if, которая
#проверит, что список пользователей не пуст.
#Если список пуст, выведите сообщение: «We need to find some users!»
#Удалите из списка все имена пользователей и убедитесь в том, что программа
#выводит правильное сообщение.
user_name_list = []
if user_name_list:
    print("Not alone")
else:
    print("We need find more users")
#5-10.  Проверка имен пользователей: выполните следующие действия для создания
#программы, моделирующей проверку уникальности имен пользователей.
#Создайте список current_users, содержащий пять и более имен пользователей.
#Создайте другой список new_users, содержащий пять и более имен пользователей.
#Убедитесь в том, что одно или два новых имени также присутствуют в списке
#current_users.
#Переберите список new_users и для каждого имени в этом списке проверьте, было
#ли оно использовано ранее.  Если имя уже использовалось, выведите сообщение о
#том, что пользователь должен выбрать новое имя.  Если имя не использовалось,
#выведите сообщение о его доступности.
#Проследите за тем, чтобы сравнение выполнялось без учета регистра символов.
#Если имя 'John’ уже используется, в регистрации имени ‘JOHN’ следует отказать.
current_users = ['john','tom','andy','randy','teddy']
new_users = ['JOHN','brad','teddy','bendy','roma']
for item in new_users:
        if item.lower() in current_users:
            print(item + " zanyat")
        else:
            print("Feel free to " + item)

#5-11.  Порядковые числительные: порядковые числительные в английском языке
#заканчиваются суффиксом th (кроме 1st, 2nd и 3rd).
#Сохраните числа от 1 до 9 в списке.
#Переберите элементы списка.
#Используйте цепочку if-elif-else в цикле для вывода правильного окончания
#числительного для каждого числа.  Программа должна выводить числительные «1st
#2nd 3rd 4th 5th 6th 7th 8th 9th», причем каждый результат должен располагаться

#в отдельной строке.
numbers = [val for val in range(1,10)]
for numb in numbers:
    if numb==1:
        print(str(numb)+"st")
    elif numb==2:
        print(str(numb)+"nd")
    elif numb==3:
        print(str(numb)+"rd")
    else:
        print(str(numb)+"th")