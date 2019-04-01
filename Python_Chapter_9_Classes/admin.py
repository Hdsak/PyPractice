from user import user
class Privileges():
    def __init__(self):
        self.privileges=["разрешено добавлять сообщения","разрешено удалять пользователей", "разрешено банить пользователей"]
    def show_privileges(self):
        for n in self.privileges:
            print(n)

class Admin(user):
    def __init__(self,first_name,last_name,user_info):
        super().__init__(first_name,last_name,user_info)
        self.privileges=Privileges()