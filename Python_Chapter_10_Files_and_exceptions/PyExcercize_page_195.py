filename="guest.txt"
#10-3. Гость: напишите программу, которая запрашивает у пользователя его имя.
#  Введенный ответ сохраняется в файле с именем guest.txt.
with open(filename,"w") as task_1:
    name=input("Input your name ")
    task_1.write(name+'\n')

#10-4. Гостевая книга: напишите цикл while, который в цикле запрашивает у пользователей имена.
#  При вводе каждого имени выведите на экран приветствие и добавьте строку с сообщением 
# в файл с именем guest_book.txt. Проследите за тем, чтобы каждое сообщение
#  размещалось в отдельной строке файла.
while True:
    with open(filename,"a") as task_1:
        name=input("Input your name ")
        if name=='q':
            break
        task_1.write(name+'\n')
#10-5. Опрос: напишите цикл while, в котором программа спрашивает у пользователя, 
# почему ему нравится программировать.
#  Каждый раз, когда пользователь вводит очередную причину, сохраните текст его ответа в файле.
while True:
    reason=input("Why do you love programming ? ")
    if reason=="q":
        break
    with open("reasons.txt","a") as reason_writter:
        reason_writter.writelines(reason)