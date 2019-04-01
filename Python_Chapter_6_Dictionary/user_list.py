user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',}
for key, value in user_0.items():
    print("Key " + key)
    print("Value " + value + "\n")
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',}
for k in favorite_languages.keys():
    print(k.title())
for v in favorite_languages.values():
    print("\n" + v.title())
friends = ['phil', 'sarah']
for n in favorite_languages:
    if n in friends:
        print("Hi " + n.title() + " your language " + favorite_languages[n])
    else:
        print(n.title())
if 'erin' not in favorite_languages.keys():
    print('Erin fuck off')
for n in sorted(favorite_languages):
    print(n.title()+' ty poe\n')
print("\nLanguages in pool\n")
for v in set(favorite_languages.values()):
    print(v.title())