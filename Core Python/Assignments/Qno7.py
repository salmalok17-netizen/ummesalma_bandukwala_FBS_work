#Write a program to find sum of digits of a number.

def sumOfDigits(n):
    sum = 0
    temp = n

    while(temp != 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + d
    return sum

num = int(input("Enter a number to find sum of digits:"))
result = sumOfDigits(num)
print(f"The sum of digits of {num} is: {result}")