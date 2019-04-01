#8-15. Печать моделей: выделите функции примера print_models.py в отдельный файл с именем printing_functions.py.
#  Разместите команду import в начале файла print_models.py и измените файл так, чтобы в нем использовались импортированные функции.
import printer
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models=[]
printer.print_model(unprinted_designs[:],completed_models)
printer.show_completed_models(completed_models)
print(unprinted_designs)
#8-16. Импортирование: возьмите за основу одну из написанных вами программ с одной функцией. Сохраните эту функцию в отдельном файле.
#  Импортируйте функцию в файл основной программы и вызовите функцию каждым из следующих способов:


#import имя_модуля

# import formate_name
# print(formate_name.get_formatted_name('Roma','Mexanik'))


#from имя_модуля import имя_функции

# from formate_name import get_formatted_name
# print(get_formatted_name("Roma",'Part 2'))


#import имя_модуля as псевдоним

# import formate_name as fn
# print(fn.get_formatted_name("roma",'part 3'))


#from имя_модуля import имя_функции as псевдоним

# from formate_name import get_formatted_name as gn
# print(gn("Roma",'part 4'))


#from имя_модуля import *

from formate_name import *
print(get_formatted_name("Roma",'part 5'))