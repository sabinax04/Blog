class User:
    users = []  

    def __init__(self, username, password, isAuthor):
        self.username = username
        self.password = password
        self.isAuthor = isAuthor

    @staticmethod
    def register():
        print("\n--- Sign Up ---")
        role_choice = input("Who are you? \n1. Author \n2. User \nChoose (1/2): ")

        username = input("Enter username: ")

        
        password_input = input("Enter password (numbers only): ")
        if not password_input.isdigit():
            print("Password must be numeric!")
            return None
        
        password = int(password_input)

        isAuthor = True if role_choice == "1" else False

        new_user = User(username, password, isAuthor)
        User.users.append(new_user)

        print(f"Account created for {username} as {'Author' if isAuthor else 'User'}.\n")
        return new_user

    @staticmethod
    def login():
        print("\n--- Login ---")
        username = input("Enter username: ")
        password_input = input("Enter password (numbers only): ")

        if not password_input.isdigit():
            print("Password must be numeric!")
            return None

        password = int(password_input)

        for user in User.users:
            if user.username == username and user.password == password:
                print(f"Welcome back, {user.username}!")
                return user

        print("Account not found!")
        choice = input("Do you want to sign up? (yes/no): ")
        if choice.lower() == "yes":
            return User.register()
        else:
            return None
        

def main():
    print("Welcome to the Blog!")

    while True:
        action = input("Do you want to (1) Login or (2) Sign Up? (type 'exit' to quit): ")

        if action == "1":
            logged_user = User.login()
            if logged_user:
                if logged_user.isAuthor:
                    print("You can view and write blog posts.")
                else:
                    print("You can only view blog posts.")
        elif action == "2":
            User.register()
        elif action.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

main()
