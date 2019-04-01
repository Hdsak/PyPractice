message="Tell me something i repeat it ." + "\nEnter 'quit' to stop "
active=True
prompt=""
while active:
    prompt=input(message)
    if prompt=='quit':
        active=False
    else:
        print(prompt)
print("Stopped")
