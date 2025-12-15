# Write a program to check if entered year is a leap year or not.

def isleap_yr(year):
    if(year % 4 == 0):
        if(year % 100 != 0):
            return True

        elif(year % 400 == 0):
            return True
    else:
        return False

year = int(input("Enter year to check leap year or not:"))
if(isleap_yr(year)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")