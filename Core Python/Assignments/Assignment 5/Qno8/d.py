#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = float(input("Enter a number:"))
sum = 0

for i in range(1, 11):
    term = (a ** i) / i
    sum = sum + term

print(f"The sum of the series is= {sum}")