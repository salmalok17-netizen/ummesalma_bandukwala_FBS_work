#WAP to print factorial of a number .

n = int(input("Enter a number to print its factorial:"))
fact = 1

for i in range(n, 0, -1):
    fact = fact * i

print(f"Factorial of {n}= {fact}")