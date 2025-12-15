# Write a program to check if given number is Armstrong or not using recursive
# function.

def armstrongSum(num, power):
    if (num <= 0):
        return 0
    else:
        digit = num % 10
        return (digit ** power) + armstrongSum(num // 10, power)

def armstrongNumber(number):
    power = len(str(number))
    calculated_sum = armstrongSum(number, power)
    return calculated_sum

def checkArmstrong(num):
    if(num == armstrongNumber(num)):
        return f"{num} is an Armstrong number."
    else:
        return f"{num} is not an Armstrong number."

num = int(input("Enter a number to check if it's an Armstrong number: "))
print(checkArmstrong(num))
