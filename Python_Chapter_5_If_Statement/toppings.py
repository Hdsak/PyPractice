requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for item in requested_toppings:
    if item == 'green peppers':
        print("Sorry we are out")
    else:
        print("You have added " + item)
print("We start coocking")

#Для всех списков, с которыми мы работали до сих пор, действовало одно простое
#предположение: мы считали, что в каждом списке есть хотя бы один элемент.
#Скоро мы предоставим пользователю возможность вводить информацию, хранящуюся в
#списке, поэтому мы уже не можем предполагать, что при каждом выполнении цикла
#в списке есть хотя бы один элемент.  В такой ситуации перед выполнением цикла
#for будет полезно проверить, есть ли в списке хотя бы один элемент.
#Проверим, есть ли элементы в списке заказанных дополнений, перед изготовлением
#пиццы.  Если список пуст, программа предлагает пользователю подтвердить, что
#он хочет базовую пиццу без дополнений.  Если список не пуст, пицца готовится
#так же, как в предыдущих примерах:
requested_toppings = []

if requested_toppings:
    for item in requested_toppings:
        print("adding " + item)
    print("we are winished")
else:
    print("Do you want plain pizza?")

#Посетители способны заказать что угодно, особенно когда речь заходит о
#дополнениях к пицце.  Что если клиент захочет положить на пиццу картофель фри?
#Списки и команды if позволят вам убедиться в том, что входные данные имеют
#смысл, прежде чем обрабатывать их.
#Давайте проверим наличие нестандартных дополнений перед тем, как готовить
#пиццу.  В следующем примере определяются два списка.  Первый список содержит
#перечень доступных дополнений, а второй — список дополнений, заказанных
#клиентом.  На этот раз каждый элемент из requested_toppings проверяется по
#списку доступных дополнений перед добавлением в пиццу:
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for item in requested_toppings:
    if item in available_toppings:
        print("You have added " + item)
    else:
        print("Fuck off " + item)
