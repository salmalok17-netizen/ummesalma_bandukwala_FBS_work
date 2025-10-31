#WAP to print all even numbers until n.

n = int(input("Enter number till you want to print even numbers:"))
i = 1
while(i <= n):
    if(i % 2 == 0):
        print(i)
    i = i + 1


