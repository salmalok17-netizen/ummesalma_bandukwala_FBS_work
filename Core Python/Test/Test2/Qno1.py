year = int(input("Enter year to check if it is leap year:"))

if(year % 4 == 0):
    if(year % 100 != 0):
        print(f"{year} is a leap year")

    elif(year % 400 == 0):
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")