# WAP to check if given number Strong Number.

n = int(input("Enter a number to check Strong:"))
num = n
sum = 0
fact = 1

while(num != 0):
    d = num % 10
    for i in range(d, 0, -1):
        fact = fact * i
    sum = sum + fact
    num = num // 10
    fact = 1

if(sum == n):
    print(f"{n} is a strong number.")
else:
    print(f"{n} is not a strong number.")
 


