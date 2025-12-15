#Sum of all prime numbers between 1 to n

def checkPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, num // 2 + 1):
        if(num % i == 0):
            return False
    else:
        return True

def sum_of_primes_up_to_n(n):
    sum = 0
    for num in range(1, n + 1):
        if checkPrime(num):
            sum = sum + num
    return sum

n = int(input("Enter a number (n): "))
result = sum_of_primes_up_to_n(n)
print(f"The sum of prime numbers from 1 to {n} is: {result}")