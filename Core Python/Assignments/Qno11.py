# WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def lengthOfNum(n):
    length = len(str(n))
    return length

def armstrong(n):
    power = lengthOfNum(n)
    sum = 0
    temp = n
    while(temp > 0):
        d = temp % 10
        sum = sum + d ** power
        temp = temp // 10
    return sum

def checkArmstrong(n):
    if(n == armstrong(n)):
        return f"{n} is an Armstrong number."
    else:
        return f"{n} is not an Armstrong number."
    
num = int(input("Enter a number to check Armstrong or not:"))
print(checkArmstrong(num))