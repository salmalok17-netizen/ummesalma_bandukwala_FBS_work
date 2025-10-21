# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a three digit number:"))
num1 = num

d1 = num1 % 10
num1 = num1 // 10 

d2 = num1 % 10
num1 = num1 // 10

d3 = num1 % 10
num1 = num1 // 10

rev = d1 * 100 + d2 * 10 + d3

if(num == rev):
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")