def word_counter(filename):
    try:
        with open(filename)as book:
            words=book.read()
    except FileNotFoundError:
        print("file "+ filename+" does not exist!")
    else:
        num_words=words.split()
        print("Book "+ filename +" contens " +str(len(num_words)))