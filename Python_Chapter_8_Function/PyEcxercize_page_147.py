#8-6. Названия городов: напишите функцию city_country(), которая получает название города и страну. 
# Функция должна возвращать строку в формате “Santiago, Chile”. 
# Вызовите свою функцию по крайней мере для трех пар «город—страна» и выведите возвращенное значение.
def city_country(city,country):
    return '"'+city+', '+country+'"'
print(city_country("Moscow","Russia"))
print(city_country("Canada","Ontario"))
print(city_country(city="Kazan",country="Russia"))
#8-7. Альбом: напишите функцию make_album(), которая строит словарь с описанием музыкального альбома.
#  Функция должна получать имя исполнителя и название альбома и возвращать словарь, содержащий эти два вида информации. 
# Используйте функцию для создания трех словарей, представляющих разные альбомы.
#  Выведите все возвращаемые значения, чтобы показать, что информация правильно сохраняется во всех трех словарях.
#Добавьте в make_album() дополнительный параметр для сохранения количества дорожек в альбоме. 
# Если в строку вызова включено значение количества дорожек, добавьте это значение в словарь альбома.
#  Создайте как минимум один новый вызов функции с передачей количества дорожек в альбоме.
def make_album(artist_name,album_name,track_count=''):
    album={'Artist':artist_name,'Album name':album_name}
    if track_count:
        album['track count']=track_count
    return album
print(make_album('Slipknot','Vermillion'))
print(make_album('Marylin Manson','HollyWood',13))
#8-8. Пользовательские альбомы: начните с программы из упражнения 8-7.
#  Напишите цикл while, в котором пользователь вводит исполнителя и название альбома. 
# Затем в цикле вызывается функция make_album() для введенных пользователей и выводится созданный словарь.
#  Не забудьте предусмотреть признак завершения в цикле while.
while True:
    print("If you want to quit press 'q'")
    artist=input("Input artist name ")
    if artist=='q':
        break
    album=input("Input album name ")
    if album=='q':
        break
    print(make_album(artist,album))

