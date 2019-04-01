class dog():
    """Simple dog model"""
    def __init__(self,name,age):
        """Initialization"""
        self.name=name
        self.age=age
    def sit(self):
        print(self.name + " is sitting")
    def roll(self):
        print(self.name+" is rolled")
my_dog=dog("Max",13)
your_dog=dog("ANdrew",21)
print("My dog name is "+my_dog.name)
print("My dog y/o is "+str(my_dog.age))
my_dog.sit()
my_dog.roll()
your_dog.roll()