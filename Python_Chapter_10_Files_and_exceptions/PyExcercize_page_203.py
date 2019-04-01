#10-6. Сложение: при вводе числовых данных часто встречается типичная проблема:
#  пользователь вводит текст вместо чисел. 
# При попытке преобразовать данные в int происходит исключение TypeError. 
# Напишите программу, которая запрашивает два числа, складывает их и выводит результат.
#  Перехватите исключение TypeError, если какое-либо из входных значений не является числом, 
# и выведите удобное сообщение об ошибке. 
# Протестируйте свою программу: сначала введите два числа, а потом введите текст вместо одного из чисел.
x=input("Print first number for addition ")
y=input("Print second number for addition ")
try:
    print(int(x)+int(y))
except ValueError:
    print("Text input")
#10-7. Калькулятор: заключите код из упражнения 10-6 в цикл while, 
# чтобы пользователь мог продолжать вводить числа,
#  даже если он допустил ошибку и ввел текст вместо числа.

while True:
    x=input("Print first number for addition ")
    y=input("Print second number for addition ")
    if x=='q' or y=='q':
        break
    try:
        print(int(x)+int(y))
    except ValueError:
        print("Text input")
#10-8. Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt. 
# Сохраните минимум три клички кошек в первом файле и три клички собак во втором.
#  Напишите программу, которая пытается прочитать эти файлы и выводит их содержимое на экран.
#  Заключите свой код в блок try-except для перехвата исключения FileNotFoundError 
# и вывода понятного сообщения об отсутствии файла.
#  Переместите один из файлов в другое место файловой системы;
#  убедитесь в том, что код блока except выполняется, как и положено.
try:
    with open("dogs.txt") as dog_name:
        for n in dog_name:
            print(n.strip())
except FileNotFoundError:
    print("File does not exist")
try:
    with open("cats.txt") as cat_name:
        for n in cat_name:
            print(n.strip())
except FileNotFoundError:
    print("File does not exist")
#10-9. Ошибки без уведомления: измените блок except из упражнения 10-8 так,
#  чтобы при отсутствии файла программа продолжала работу, не уведомляя пользователя о проблеме.
try:
    with open("dogs.txt") as dog_name:
        for n in dog_name:
            print(n.strip())
except FileNotFoundError:
    pass
try:
    with open("cats.txt") as cat_name:
        for n in cat_name:
            print(n.strip())
except FileNotFoundError:
    pass
#10-10. Частые слова: зайдите на сайт проекта «Гутенберг» (http://gutenberg.org/) 
# и найдите несколько книг для анализа. Загрузите текстовые файлы этих произведений 
# или скопируйте текст из браузера в текстовый файл на вашем компьютере.
#Для подсчета количества вхождений слова или выражения в строку можно воспользоваться методом count().
#  Например, следующий код подсчитывает количество вхождений ‘row’ в строке:
#>>> line = "Row, row, row your boat"
#>>> line.count('row')
#2
#>>> line.lower().count('row')
#3
#Обратите внимание: преобразование строки к нижнему регистру функцией lower() позволяет 
# найти все вхождения искомого слова независимо от регистра.
#Напишите программу, которая читает файлы из проекта «Гутенберг» и
#  определяет количество вхождений слова ‘the’ в каждом тексте.
print("\n Task 10\n")
while True:
    x=input("Input word for analysis ")
    with open("poland.txt") as book:
        words=book.read()
        count=words.count(x)
    with open("road.txt") as book:
        words=book.read()
        count+=words.count(x)
    with open("quarter.txt") as book:
        words=book.read()
        count+=words.count(x)
    print(count)