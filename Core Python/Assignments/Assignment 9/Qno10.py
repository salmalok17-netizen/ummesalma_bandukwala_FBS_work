# Write a program to reverse a number using recursion.

def reverseNo(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(reverseNo(n // 10)))

num = int(input("Enter a number: "))
reversed_num = reverseNo(num)
print("Reversed number:", reversed_num)
