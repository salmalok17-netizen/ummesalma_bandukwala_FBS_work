num = int(input("Enter a three digit number:"))
num1 = num

d1 = num1 % 10
num1 = num1 // 10 

d2 = num1 % 10
num1 = num1 // 10

sum = d1 +d2 + num1
print(f'Sum of {num} is: {sum}')