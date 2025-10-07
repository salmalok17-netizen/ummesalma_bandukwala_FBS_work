num = 123
print(num)
num2 = num

d1 = num2 % 10
num2 = num2 // 10

d2 = num2 % 10
num2 = num2 // 10

d3 =num2 % 10
num2 = num2 // 10

rev = d1*100 + d2*10 + d3
print(rev)