# Write a program to check if entered number is a palindrome or
# not.

def palindrome(n):
    temp = n
    reversed_num = 0
    while(temp > 0):
        remainder = temp % 10
        reversed_num = (reversed_num * 10) + remainder
        temp = temp // 10
    return reversed_num

num = int(input("Enter a number to check palindrome:"))
rev_num = palindrome(num)
if(num == rev_num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")