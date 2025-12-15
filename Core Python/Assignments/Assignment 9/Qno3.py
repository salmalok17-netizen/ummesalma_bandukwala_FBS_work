# Write a program to reverse a given number using recursive function.

def reverseNumber(num):
  if num < 10:
    return num
  else:
    return (str(num % 10) + str(reverseNumber(num // 10)))

num = int(input("Enter a number: "))
reversed_num = reverseNumber(num)
print("Reversed number:", reversed_num)