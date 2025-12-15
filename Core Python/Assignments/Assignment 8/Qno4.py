#Sum of all odd numbers between 1 to n

def sumOfOddNum(n):
    sum = 0
    for i in range(1, n+1):
        if(i % 2 != 0):
            sum = sum + i
    return sum

n = int(input("Enter number till you want the sum:"))
result = sumOfOddNum(n)
print(f"The sum of all odd numbers between 1 to {n} is: {result}")
