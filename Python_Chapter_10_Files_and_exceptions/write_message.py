filename="empty_file_for_now.txt"
with open(filename,'w')  as  writter_example:
    writter_example.write("I love python. \n")
    writter_example.write("I love cocks\n")
with open(filename,"a") as addition:
    addition.write("This string is example of addition\n")
    addition.write("Another addition example\n")
    