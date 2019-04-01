class user():
    """User class"""
    def __init__(self,first_name,last_name,user_info):
        self.first_name=first_name
        self.last_name=last_name
        self.user_info=user_info
    def describe_user(self):
        print("Name "+ self.first_name+ "\nLast name "+self.last_name)
        # for k,v in self.user_info.items():
        #     print(k.title()+" "+str(v))
    def greet_user(self):
        print("Hey "+self.first_name)
