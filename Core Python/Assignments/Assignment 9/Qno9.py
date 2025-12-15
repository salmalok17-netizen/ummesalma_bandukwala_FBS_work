# Write a program to calculate the m to the power n using recursion.

def power(m , n):
    if(n == 0):
        return 1
    else:
        return m * power(m , n - 1)
    
base = int(input("Enter a number for base number:"))
exponent = int(input("Enter a number for exponent number:"))
result = power(base, exponent)
print(f"{base} to the power of {exponent} is: {result}")

    