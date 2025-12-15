# Write a program to find sum of n numbers using recursion.

def sumOfNNum(n):
    if(n <= 0):
        return 0
    else:
        return (n + (sumOfNNum(n-1)))
    
n = int(input("Enter value for sum of n numbers:"))
result = (sumOfNNum(n))
print(result)