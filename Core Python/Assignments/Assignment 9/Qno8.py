# Write a program to check whether a number is prime or not using recursion.

def checkPrime(n , i = 2):
    if(n <= 1):
        return False
    elif(n == i):
        return True
    else:
        if(n % i == 0):
            return False
        else:
            return checkPrime(n , i + 1)
        
num = int(input("Enter a number to check prime or not:"))
if(checkPrime(num)):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
            


