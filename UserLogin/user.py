class User:
    def __init__(self, username, password, isAuthor):
        self.username = username
        self.password = password
        self.isAuthor = isAuthor
    
    @staticmethod
    def register():
        role_choice = input("Are you author or username: \n"
                         + "1. Author \n"
                         + "2. User \n"
                         + "Choose one number ! ")
        
        username = input("Please enter your username: ")
        password = int(input("Please enter your password (as number): "))

        if role_choice == "1":
            isAuthor = True
        else:
             isAuthor = False
        
        return User(username, password, isAuthor)
    

    def login(self):
        newUserName = input("Please enter your username: ")
        newPassword = int(input("Please enter your password: "))

        if self.username == newUserName and self.password == newPassword:
            print("Welcome to our blog, " + self.username)
        
        else:
            print("We didn't find your account !")
            question = input("Do you want to create your account ? (yes / no)")

            if question.lower() == "yes":
                new_user = User.register()
                print("Account is created for " + new_user.username)
       
                
new_user = User.register()
new_user.login()