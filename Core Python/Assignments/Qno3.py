# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

# a. 1+ 2 + 3 + 4+..... + n
def sumOfSeries(n):
    sum = 0
    for i in range(1 , n+1):
        sum = sum + i
    return sum

# b. 1!+ 2! + 3! + 4!+..... + n!
def sumOfFact(n):
    fact = 1
    sum = 0
    for i in range(1, n+1):
        fact = fact * i
        sum = sum + fact
    return sum

# c. 1^1 + 2^2 + 3^3+ ...... n^n
def sumOfPower(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i ** i
    return sum

n = int(input("Enter number till you want sum of the series:"))
a = sumOfSeries(n)
b = sumOfFact(n)
c = sumOfPower(n)
print(f"The sum of numbers up to {n} is: {a}")
print(f"The sum of factorials series up to {n} is: {b}")
print(f"The sum of power series up to {n} is: {c}")

