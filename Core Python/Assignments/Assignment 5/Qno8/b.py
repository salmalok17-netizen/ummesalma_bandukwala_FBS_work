# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n = int(input('Enter a number:'))
sum = 0

for i in range(1, n + 1):
    sum = sum + n ** i

print(f"The sum of series of {n} is= {sum} ")