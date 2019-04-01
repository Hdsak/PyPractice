users={
    'einstein':{
        'first':'albert',
        'last':'einstein'
        ,'location':'paris'},
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'}}
for username, info in users.items():
    print("Username : " + username.capitalize())
    for k,v in info.items():
        print("\t"+k.title()+" "+v.capitalize())

