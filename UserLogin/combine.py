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
                print(f"Welcome back, {user.username}!\n")
                return user

        print("Account not found!")
        choice = input("Do you want to sign up? (yes/no): ")
        if choice.lower() == "yes":
            return User.register()
        else:
            return None


class Blog:
    all_blogs = []
    personal_blogs=[]

    def __init__(self, id, title, content, author=None):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        Blog.all_blogs.append(self)

    def show(self):
        return {
            "ID": self.id,
            "Title": self.title,
            "Content": self.content,
            "Author": self.author.username
        }

    @staticmethod
    def get_blog():
        if not Blog.all_blogs:
            print("No blogs available\n")
        else:
            print("\n--- Blog List ---")
            for blog in Blog.all_blogs:
                print(blog.show())
            print()

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Content: {self.content}, Author: {self.author.username}"

    @staticmethod
    def create_blog(author):
        
        if not author.isAuthor:
            print("You are not allowed to create blogs.\n")
            return None

        title = input("Enter your blog title: ")
        content = input("Enter your blog content: ")
        id = len(Blog.all_blogs) + 1
        new_blog = Blog(id, title, content, author)

        Blog.personal_blogs.append(new_blog)

        print(f"\n{new_blog} is created successfully!\n")
        return new_blog

    @staticmethod
    def default_blogs():
        user1 = User("john_doe", 1234, isAuthor=True)
        blog1 = Blog(1, "Recipes", "How to cook cupcakes", user1)
        blog2 = Blog(2, "Vlog", "One day with me during midterm session", user1)

    @staticmethod
    def get_my_personal_blogs():
        if not Blog.personal_blogs:
            print("you dont have any blog")
        else:
            for blog in Blog.personal_blogs:
                print(blog.show())

    @staticmethod
    def update_blog(blog,new_title=None,new_content=None):
        if not Blog.personal_blogs:
            return None
        if new_title:
            blog.title=new_title
        if new_content:
            blog.content=new_content
        print(f"Blog '{blog.title}' updated successfully!")

                


def main():
    Blog.default_blogs()

    print("Welcome to the Blog!")

    while True:
        action = input("Do you want to (1) Login or (2) Sign Up? (type 'exit' to quit): ")

        if action == "1":
            logged_user = User.login()
        elif action == "2":
            logged_user = User.register()
        elif action.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Invalid choice!")
            continue

        if not logged_user:
            continue

       
        while True:
            if logged_user.isAuthor:
                print("\nWhat do you want to do?")
                print("1. View all blogs")
                print("2. Create a blog")
                print("3. Logout")
                print("4. View my blogs")
                print("5. Update your blog")
                choice = input("Choose (1/2/3/4/5): ")

                if choice == "1":
                    Blog.get_blog()
                elif choice == "2":
                    Blog.create_blog(logged_user)
                elif choice == "3":
                    print("Logged out.\n")
                    break
                elif choice=="4":
                    Blog.get_my_personal_blogs()
                elif choice=="5":
                        update=input("Do you want to update your blog? 1.yes 2.no ")
                        if update=="1":
                            blog_id=input(f"enter the id of blog you want to update: ")
                            blog_to_update=0
                            for blog in Blog.personal_blogs:
                                if str(blog.id)==blog_id:
                                    blog_to_update=blog
                                    break
                            if blog_to_update:
                                new_title=input(f"enter new title instead {blog_to_update.title} : ")
                                new_content=input(f"enter new content instead {blog_to_update.content} : ")

                                Blog.update_blog(blog_to_update,new_title,new_content)
                        elif update=="2":
                            break
                else:
                    print("Invalid choice!")
            else:
                print("\nYou can only view blogs.")
                Blog.get_blog()
                print("Logging out...\n")
                break
       

main()
