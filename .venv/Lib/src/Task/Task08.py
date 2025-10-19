#Check if the user can log in based on correct username and password.

#I/p
#username = "admin"  password = "1234"

user_name=input("Enter your user name: ")
password=input("Enter your password: ")
if user_name=="admin" and password==1234:
    print("Successfully logged in")
else: print("Please check your credentials")

