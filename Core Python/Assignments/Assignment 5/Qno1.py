# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

uid = "abc123"
pwd = "qwerty"

for i in range(1, 4):
    user_id = input("Enter username:")
    password = input("Enter password:")
    print()

    if(user_id == uid and password == pwd):
        print("Login Successfull!")
        break
    else:
        print("Incorrect Username or Password. Please try again!")
        print("-" * 40)

else:
    print("Too many wrong attempts. Try again Later.")