#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)

import random
userid = "abc123"
pwd = "uabc123"

uid= (input("Enter userid:"))
passwrd = (input("Enter password:"))

if(uid == userid) and (passwrd == pwd):
    print(f"Login Successfull!")

    captcha = str(random.randint(1111,9999))
    print(f"Please enter the following 4 digit number: {captcha}")
    entered_captcha = input("Enter the number:")

    if(entered_captcha == captcha):
         print("Captcha verified successfully! Access granted.")
    else:
            print("Incorrect captcha. Access denied.")

else:
    print(f"Invalid Userid or Password")