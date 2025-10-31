# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter the number of terms:"))

sum = 1 * (2**n - 1) / (2 - 1)
print(f"The sum of the geometric series from 1 to {n} with the ratio 2 is = {sum}")