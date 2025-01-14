from user import User
import time
class user_management():
    def __init__(self):
        self.users = []
    def add_user(self,username,password):
        user = User(username,password)
        self.users.append(user)

    def login(self,username,password):
        flag = False
        for user in self.users:
            if user.username == username:
                if user.password == password:
                    print("Login Sucessfully ",end='')
                    for i in range(15):
                        time.sleep(0.1)
                        print(".", end='', flush=True)  # flush=True ensures the print happens immediately
                    print()  # Move to the next line after the animation finishes
                    return True
                else:
                    print("wrong password")
                    flag = True
        if not flag : 
            print("User Not Found !!!")
