# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

n = int(input("Enter a number to check Armstrong:"))
num = n
num2 = n
sum = 0
count = 0

while(num > 0):
    d = num % 10
    num = num // 10
    count = count + 1
    
for i in range(1, count + 1):
    d2 = 1
    d1 = num2 % 10
    for j in range(1, count + 1):
        d2 = d2 * d1
    sum = sum + d2
    num2 = num2 // 10

if(n == sum):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")


