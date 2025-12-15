# Write a program to find factorial using recursion.

def fact(n):
    if(n == 0):
        return 1
    elif(n < 0):
        return f"{n} is a negative number."
    else:
        return n * fact(n-1)
    
n = int(input("Enter a number:"))
result = fact(n)
print(result)