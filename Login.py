import gspread
from oauth2client.service_account import ServiceAccountCredentials
import hashlib

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("GoogleCreds.json", scope)
client = gspread.authorize(creds)
Sheet = client.open("User Accounts").sheet1
UserList = Sheet.get_all_records()

def hash(Pword):
    Pword = Pword.encode("utf-8")
    Pword = hashlib.md5(Pword)
    Pword = Pword.hexdigest()
    return Pword

def login():
    userfound = False
    print("Login to Artiviewer Now!")
    username = input("Please input your username: ")
    UsernameList = Sheet.col_values(1)
    for index, user in enumerate(UsernameList):
        if (user == username):
            userfound = True
            print("Username found")
            hashedpassword = Sheet.cell(index+1,2).value
    if(userfound==False):
        print("Username was not found, please register")
        register()
    password = input("Please input your password: ")
    if (hashedpassword == hash(password)):
        print("Access Granted")
    else:
        print("Incorrect Password, please try again")

def register():
    print("Register Now!")
    username = input("Please input a username: ")
    password = input("Please choose a password: ")
    password = hash(password)
    email = input("Please input your email: ")
    insertDetails = [username,password,email]
    Sheet.insert_row(insertDetails,2)

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
#Get specific row
#row = Sheet.row_values(2)
#Get specific cell
#cell = Sheet.cell(2,2).value
#pprint(cell)