# Write a program to print first n prime numbers.

n = int(input("How many first prime numbers you want to print:"))
count = 0
num = 2

while(count < n):
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(num, end = " ")
        count += 1
    num = num + 1