# Write a program to find sum of digits using recursion.

def sumOfDig(num):
    if(num <= 0):
        return 0
    else:
        return (num % 10) + sumOfDig(num // 10)
       
n = int(input("Enter a number:"))
print(sumOfDig(n))