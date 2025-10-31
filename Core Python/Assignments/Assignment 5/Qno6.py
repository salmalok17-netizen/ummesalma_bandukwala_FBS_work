# Write a program to print prime numbers between 1 to 100.

for n in range(2, 101):
    for i in range(2,n):
        if(n % i == 0):
            break
    else:
        print(n, end = " ")

