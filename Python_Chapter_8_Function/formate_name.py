def get_formatted_name(first,last,middle=''):
    "Return full formatted name"
    full_name=first.title()+" "+middle.title()+" "+last.title()
    return full_name
# my_name=get_formatted_name('roma','mexanik')
# print(my_name)
# print(get_formatted_name('max','maximov'))
# print(get_formatted_name('Kurt','Cobain','lol'))
# while True:
#     print("(enter 'q' at any time to quit)")
#     name=input("Input your name ")
#     if name=='q':
#         break
#     last=input("Input your last name ")
#     if last=='q':
#         break
#     print("Hello "+ get_formatted_name(name,last))