# WAP to print Fibonacci series upto n.

n = int(input("Enter a number to get the Fibonacci series up to that term: "))

a,b = 0,1
i = 0

print("Fibonacci series:")
while(i < n):
    print(a, end=' ')
    next_term = a + b
    a = b
    b = next_term
    i += 1