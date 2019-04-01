with open('text_files/text_file_example.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())
with open("pi_digits.txt") as line_example:
    for line in line_example:
        print(line.rstrip())
with open("pi_digits.txt") as third_example:
    lines=third_example.readlines()
    print(lines)
    for line in lines:
        print(line)
pi_string=""
for line in lines:
    pi_string+=line.rstrip()+" "

print(pi_string)
print(len(pi_string))
birth_day=input("Input your bith day format ddmmyy : ")
if birth_day in pi_string.strip():
    print("Your birth day in pi number")
else:
    print("Your birthday not appears in pi number")