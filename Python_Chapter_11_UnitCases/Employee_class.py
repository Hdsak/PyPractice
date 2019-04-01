class Employee():
    """Class of employee"""
    def __init__(self,name,last,salary):
        self.name=name
        self.last=last
        self.salary=salary
    def give_raise(self,money=5000):
        self.salary+=money