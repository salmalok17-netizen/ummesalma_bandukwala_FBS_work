#Write a program to check if user has entered correct userid and password.

userid = "abc123"
pwd = "uabc123"

uid= (input("Enter userid:"))
passwrd = (input("Enter password:"))

if(uid == userid) and (passwrd == pwd):
    print(f"Login Successfull!")
else:
    print(f"Invalid Userid or Password")