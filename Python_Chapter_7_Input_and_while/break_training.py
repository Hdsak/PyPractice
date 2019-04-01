prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
message=""
while True:
    message=input(prompt)
    if message=='quit':
        break
    else:
        print(message)
