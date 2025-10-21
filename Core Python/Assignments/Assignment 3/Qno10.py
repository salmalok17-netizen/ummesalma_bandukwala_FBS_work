#Write a program to check if person is eligible to marry or not (male age >=21 and
#female age>=18)

age = int(input("Enter age:"))
gender = input("Enter Gender (male / female):")

if(gender == 'male'):
    if(age >= 21):
        print(f"Yor are eligible for marriage")
    else:
        print(f"You are not eligible for marriage")

elif(gender == 'female'):
    if(age >= 18):
        print(f"Yor are eligible for marriage")
    else:
        print(f"You are not eligible for marriage")
