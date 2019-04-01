#10-11. Любимое число: напишите программу, которая запрашивает у пользователя его любимое число. 
# Воспользуйтесь функцией json.dump() для сохранения этого числа в файле. 
# Напишите другую программу, которая читает это значение и выводит сообщение: 
# «Я знаю ваше любимое число! Это _____».
print("\nTask 1\n")
import json
filename="favorite_number.json"
fav_number=input("Input your favorite number :")
with open(filename,"w") as fav_json:
    json.dump(fav_number,fav_json)
with open(filename) as fav_json:
    json_fav_number=json.load(fav_json)
print("Your fav number is " +json_fav_number)

#10-12. Сохраненное любимое число: объедините две программы из упражнения 10-11 в один файл.
#  Если число уже сохранено, сообщите его пользователю,
#  а если нет — запросите любимое число пользователя и сохраните в файле.
#  Выполните программу дважды, чтобы убедиться в том, что она работает.
print("\nTask 2\n")
filename="task_2_json.json"
try:
    with open(filename) as fav_json:
        json_fav_number=json.load(fav_json)
        print("yur fav number is "+ str(json_fav_number))
except:
    x=input("Oh i dont know you please input your fav number : ")
    with open(filename,"w") as fav_json:
        json.dump(x,fav_json)
#10-13. Проверка пользователя: последняя версия remember_me.py предполагает,
#  что пользователь либо уже ввел свое имя, либо программа выполняется впервые.
#  Ее нужно изменить на тот случай, если текущий пользователь не является тем человеком,
#  который последним использовал программу.
#Прежде чем выводить приветствие в greet_user(),
#  спросите пользователя, правильно ли определено имя пользователя. 
# Если ответ будет отрицательным, вызовите get_new_username()
#  для получения правильного имени пользователя.
print("\nTask 3\n")
def get_stored_username():
    try:
        with open("user_task_3.json") as get_user:
            username=json.load(get_user)
            return username
    except FileNotFoundError:
        print("Oh i dont remeber you ")
def get_new_username():
    filename="user_task_3.json"
    user=input("What is your name? ")
    with open(filename,"w") as new_user:
        json.dump(user,new_user)
        return user
def greet_user():
    username=get_stored_username()
    if username:
        ans=input("Are you "+ username+"?")
        if ans.lower()=="no":
            username=get_new_username()
        else:
            print("Hi "+ username)
    else:
        username=get_new_username()
    print("I'll remember you "+username)
greet_user()