num = int(input("Enter a three digit number:"))
temp = num

if(num != 0):
    d3 = temp % 10
    temp = temp // 10
    d2 = temp % 10
    d1 = temp // 10

    if(d1 == d2 * 2 and d1 == d3 / 2):
        print(f"Yes, you have done it")
    else:
        print(f"Please try next time")

