# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

n = int(input("Enter the number of terms:"))
x = float(input("Enter the value of x:"))
sum = 0

for i in range(n):
    sign = (-1)**i
    power_of_x = x**(i + 1)
    denominator = 2 * i + 1
    term = sign * (power_of_x / denominator)
    sum = sum + term

print(f"The sum of the series to {n} terms is: {sum}")