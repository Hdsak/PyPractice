unconfirmed_users=['alice', 'brian', 'candace']
confirmed_users=[]
while unconfirmed_users:
    user=unconfirmed_users.pop()
    print("Veryfiengdggs " + user.title())
    confirmed_users.append(user)
print("This users a confirmed")
for n in confirmed_users:
    print("\t"+n.title())
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)
