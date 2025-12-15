#Write a program find reverse of a number

def reverse(n):
    temp = n
    reversed_num = 0
    while(temp > 0):
        remainder = temp % 10
        reversed_num = (reversed_num * 10) + remainder
        temp = temp // 10
    return reversed_num

num = int(input("Enter any number: "))
result = reverse(num)
print(f"The reversed number of {num} is: {result}")