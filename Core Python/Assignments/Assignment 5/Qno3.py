# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n = int(input("Enter number of passengers:"))
ticketamt = float(input("Enter per person ticket amount:"))
total_fare = 0

for i in range(1, n+1):
    age = int(input(f"Enter age of person {i}:"))
    if(age < 12):
        price = ticketamt * 70 / 100
    elif(age > 59):
        price = ticketamt * 50 / 100
    else:
        price = ticketamt

    print(f"Ticket price of person {i} = Rs.{price}")
    total_fare = total_fare + price
    print()

print(f"Total fare of all tickets = Rs.{total_fare}")
