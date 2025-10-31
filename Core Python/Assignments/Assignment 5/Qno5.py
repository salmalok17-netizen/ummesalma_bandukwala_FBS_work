# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)

amt = float(input("Enter amount:"))
temp = amt
total = 0

for i in range(2000, 9, -10):
    if(i == 2000 or i == 500 or i == 200 or i == 100 or i == 50 or i == 20 or i == 10):
        note = temp // i
        temp = temp % i
        total = total + note

print(f'Minimum no. of notes required for {amt} is {total}')

