message=input("Tell me something and i repeat it back : ")
print(message)
prompt="If you tell us who you are, we can personalize the messages you see."+"\nWhat is your first name?"
name=input(prompt)
print("hello " + name)
age=input("How old are you: ")
age=int(age)
if age>20:
    print("Die already")
else:
    print("Live")
