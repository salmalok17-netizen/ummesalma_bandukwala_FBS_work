#swapping using third variable

x = 10
y = 20
#print(f"Before swapping value of x is {x} & y is {y}")

z = x
x = y
y = z
#print(f"After swapping value of x is {x} & y is {y}")


#swapping without third variable

x = 10
y = 20
print(f"Before swapping value of x= {x} & y= {y}")

#x = x + y
#y = x - y
#x = x - y

x,y = y,x
print(f"After swapping value of x= {x} & y= {y}")