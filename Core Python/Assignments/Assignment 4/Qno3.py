#WAP to print sum of series upto n.

n = int(input("Enter value of n to print sum of series upto n:"))
sum = 0

for i in range(1, n+1):
    sum = sum + i
print(f"Addition is= {sum}")
