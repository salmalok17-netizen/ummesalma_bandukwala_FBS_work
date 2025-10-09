x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

print("Before Swapping:")
print(f"x = {x}")
print(f"y = {y}")

x = x + y
y = x - y
x = x - y

print("After Swapping:")
print(f"x = {x}")
print(f"y = {y}")