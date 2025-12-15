# Write a program to print Fibonacci series using recursion.

def fibonacciRecursive(n):
    if n <= 1:
        return n
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

def fibonacciSeries(n):
    if n <= 0:
        print("Please enter a positive number of terms.")
    else:
        print("Fibonacci Series:")
        for i in range(n):
            print(fibonacciRecursive(i), end=" ")
        print() 


terms = int(input("Enter the number of terms for the Fibonacci series: "))
fibonacciSeries(terms)
