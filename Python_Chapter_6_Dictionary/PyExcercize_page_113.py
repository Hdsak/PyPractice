#6-4.  Глоссарий 2: теперь, когда вы знаете, как перебрать элементы словаря,
#упростите код из упражнения 6-3, заменив серию команд print циклом,
#перебирающим ключи и значения словаря.  Когда вы будете уверены в том, что
#цикл работает, добавьте в глоссарий еще пять терминов Python.  При повторном
#запуске программы новые слова и значения должны быть автоматически включены в
#вывод.
prog_dict = {
    'АРМ':'Место оператора, оборудованное всеми средствами, необходимыми для выполнения определённых функций. В системах обработки данных и учреждениях обычно АРМ — это дисплей с клавиатурой, но может использоваться также и принтер, внешние ЗУ и др.',
    'АОС':'Комплексы программно-технических и учебно-методических средств, обеспечивающих активную учебную деятельность: обучение конкретным знаниям, проверку ответов учащихся, возможность подсказки, занимательность изучаемого материала.',
    'Адаптер':'Устройство связи компьютера с периферийными устройствами.',
    'Адрес':'Номер конкретного байта оперативной памяти компьютера.',
    'Алгоpитм':'Заранее заданное понятное и точное предписание возможному исполнителю совершить определенную последовательность действий для получения решения задачи за конечное число шагов.'}
for k,n in prog_dict.items():
    print(k + " : " + n+"\n")

#6-5.  Реки: создайте словарь с тремя большими реками и странами, по которым
#протекает каждая река.  Одна из возможных пар «ключ—значение» — ‘nile’:
#‘egypt’.
#Используйте цикл для вывода сообщения с упоминанием реки и страны — например,
#«The Nile runs through Egypt.»
#Используйте цикл для вывода названия каждой реки, включенной в словарь.
#Используйте цикл для вывода названия каждой страны, включенной в словарь.
rivers={'nile':'egypt',
        'lena':'russia',
        'amazon':'USA'}
for r,n in rivers.items():
    print("The " + r.capitalize()+" runs trough "+ n.capitalize())
for n in rivers:
    print("\nRivers " + n.capitalize())
for n in rivers.values():
    print("\nCountry "+ n.capitalize())
#6-6.  Опрос: Возьмите за основу код favorite_languages.py (с.  106).
#Создайте список людей, которые должны участвовать в опросе по поводу любимого
#языка программирования.  Включите некоторые имена, которые уже присутствуют в
#списке, и некоторые имена, которых в списке еще нет.
#Переберите список людей, которые должны участвовать в опросе.  Если они уже
#прошли опрос, выведите сообщение с благодарностью за участие.  Если они еще не
#проходили опрос, выведите сообщение с предложением принять участие.
fav_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby'
    ,'phil':'python'}
must_to_join=['roma','jen','phil','max','carf']
for k in must_to_join:
    if k in fav_languages.keys():
        print(k.title()+" Ty for the pool\n")
    else:
        print(k.title()+" would you like to sign my petition?\n")
