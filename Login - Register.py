

def login():
    print("Login to Artiviewer Now!")
    username = input("Please input your username: ")
    password = input("Please input your password: ")
def register():
    print("Register Now!")
    username = input("Please input a username: ")
    password = input("Please choose a password: ")
    email = input("Please input your email: ")

def begin():
    global selection
    print("Welcomer to Artiviewer")
    option = input("Do you have an account or would you like to register? ")
    option = option.lower()
    if(option!= "login" and option!="register"):
        begin()
    if(option == "login"):
        login()
    else:
        register()


begin()