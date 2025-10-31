# WAP to print all numbers in a range divisible by a given number.

n = int(input("Enter a number to print its divisible numbers:"))
start = int(input("Enter number from you want to print number:"))
end = int(input("Enter number till you want to print number:"))

for i in range(start, end+1):
    if(i % n == 0):
        print(i)
    i = i + 1