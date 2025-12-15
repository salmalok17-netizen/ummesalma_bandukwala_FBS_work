# Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibonacci(n):
    a,b = 1,1
    i = 1

    while(i < n):
        print(a, end=' ')
        next_term = a + b
        a = b
        b = next_term
        i += 1

n = int(input("Enter a number for n terms:"))
result = fibonacci(n)
