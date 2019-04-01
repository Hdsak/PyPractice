#6-7.  Люди: начните с программы, написанной для упражнения 6-1 (с.  107).
#Создайте два новых словаря, представляющих разных людей, и сохраните все три
#словаря в списке с именем people.  Переберите элементы списка людей.  В
#процессе перебора выведите всю имеющуюся информацию о каждом человеке.
person_01 = {
    'first_name':'Maxim',
    'last_name': 'LolKg',
    'age':13,
    'city':'Kazan'}
person_02 = {
    'first_name':'Roma',
    'last_name': 'MExab',
    'age':22,
    'city':'Canada'}
person_03 = {
    'first_name':'AMer',
    'last_name': 'Vatnik',
    'age':44,
    'city':'USA'}
persons = [person_01,person_02,person_03]
for n in persons:
    print("Person : ")
    for k,v in n.items():
        print("\t" + k.title() + " : " + str(v).capitalize())
#6-8.  Домашние животные: создайте несколько словарей, имена которых
#представляют клички домашних животных.  В каждом словаре сохраните информацию
#о виде животного и имени владельца.  Сохраните словари в списке с именем pets.
#Переберите элементы списка.  В процессе перебора выведите всю имеющуюся
#информацию о каждом животном.
bob = {
    'specie':"dog",
    'owner':'Tim'}
archie = {
    'specie':"cat",
    'owner':'Andrew'}

martie = {
    'specie':"dog",
    'owner':'Lucia'}

Tomoshka = {
    'specie':"cat",
    'owner':'Roma'}
pets = [bob,archie,martie,Tomoshka]
for n in pets:
    print(str(n))

#6-9.  Любимые места: создайте словарь с именем favorite_places.  Придумайте
#названия трех мест, которые станут ключами словаря, и сохраните для каждого
#человека от одного до трех любимых мест.  Чтобы задача стала более интересной,
#опросите нескольких друзей и соберите реальные данные для своей программы.
#Переберите данные в словаре, выведите имя каждого человека и его любимые
#места.
fav_places = {
    'italy':"Max",
    'Canada':"Roma",
    'Romania':'Octavian'}
for k,n in fav_places.items():
    print(n.title() + " love " + k.capitalize())

#6-10.  Любимые числа: измените программу из упражнения 6-2 (с.  107), чтобы
#для каждого человека можно было хранить более одного любимого числа.  Выведите
#имя каждого человека в списке и его любимые числа.
fav_numbers = {
    "andrew":[1,2,3],
    'max':[4,5,6],
    'roma':[7],
    'Timur':[8,9],
    'Evgeniy':[10]}
for k,n in fav_numbers.items():
    print(k.title() + " favorite numbers are: ")
    for it in n:
        print("\t" + str(it))

#6-11.  Города: создайте словарь с именем cities.  Используйте названия трех
#городов в качестве ключей словаря.  Создайте словарь с информацией о каждом
#городе; включите в него страну, в которой расположен город, примерную
#численность населения и один примечательный факт, относящийся к этому городу.
#Ключи словаря каждого города должны называться country, population и fact.
#Выведите название каждого города и всю сохраненную информацию о нем.
city_info_01 = {
    "country":"russia",
    "population":155555,
    'fact':"Musa"}
city_info_02 = {
    "country":"USA",
    "population":2000,
    'fact':"IDGAF"}
city_info_03 = {
    "country":"russia",
    "population":535434,
    'fact':"Put"}
cities = {
    'Kazan': city_info_01,
    'NY':city_info_02,
    "Moscow":city_info_03}
for k,v in cities.items():
    print("\n" + k.capitalize() + " info")
    for n,t in v.items():
        print(n.capitalize() + " is " + str(t).title())

