#8-1. Сообщение: напишите функцию display_message() для вывода сообщения по теме, рассматриваемой в этой главе.
# Вызовите функцию и убедитесь в том, что сообщение выводится правильно.
def display_message():
    """Output by theme"""
    print("Python is amazing")

#8-2. Любимая книга: напишите функцию favorite_book(), которая получает один параметр title. 
# Функция должна выводить сообщение вида «One of my favorite books is Alice in Wonderland». 
# Вызовите функцию и убедитесь в том, что название книги правильно передается как аргумент при вызове функции.
def favorite_book(tittle):
    print("One of my favorite books is "+tittle)

display_message()
favorite_book("Fight club")
