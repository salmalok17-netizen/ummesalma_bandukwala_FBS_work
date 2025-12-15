# Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

def fact(n):
    if(n == 0):
        return 1
    elif(n < 0):
        return f"{n} is a negative number."
    else:
        return n * fact(n-1)
    
def sumOfFact(n):
    if (n <= 0):
        return 0
    else:
        return fact(n) + sumOfFact(n - 1)
    
num = int(input("Enter a number till you want sum of factorials:"))
result = sumOfFact(num)
print(f"The sum of factorial series till {num}! is : {result}")