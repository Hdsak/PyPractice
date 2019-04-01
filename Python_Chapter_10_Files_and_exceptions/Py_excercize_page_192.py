#10-1. Изучение Python: откройте пустой файл в текстовом редакторе и 
# напишите несколько строк текста о возможностях Python.
#  Каждая строка должна начинаться с фразы: «In Python you can…»
#  Сохраните файл под именем learning_python.txt в каталоге,
#  использованном для примеров этой главы. Напишите программу,
#  которая читает файл и выводит текст три раза: с чтением всего файла,
#  с перебором строк объекта файла и с сохранением строк в списке с последующим выводом
#  списка вне блока with.
with open("learning_python.txt") as example_1:
    task_1=example_1.read()    
    print(task_1)
with open ("learning_python.txt") as example_1:
    #Task 2
    for line in example_1:
        print(line)
    #task 3
with open("learning_python.txt") as example_1:
    lines=example_1.readlines()
    print(lines)
#10-2. Изучение C: метод replace() может использоваться для замены любого слова в строке другим словом.
#  В следующем примере слово ‘dog’ заменяется словом ‘cat’:
#>>> message = "I really like dogs."
#>>> message.replace('dog', 'cat')
#'I really like cats.'
#Прочитайте каждую строку из только что созданного файла learning_python.txt 
# и замените слово Python названием другого языка, например C.
#  Выведите каждую измененную строку на экран.
with open("learning_python.txt") as task_2:
    for line in task_2:
        print(line.replace("python","c"))