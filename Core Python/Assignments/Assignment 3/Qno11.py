#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.


ticketamt = float(input("Enter per person ticket amount:"))

per1 = int(input("Enter age of person  1:"))
if(per1 < 12):
    price1 = ticketamt * 70 / 100
elif(per1 > 59):
    price1 = ticketamt * 50 / 100
else:
    price1 = ticketamt

per2 = int(input("Enter age of person  2:"))
if(per2 < 12):
    price2 = ticketamt * 70 / 100
elif(per2 > 59):
    price2 = ticketamt * 50 / 100
else:
    price2 = ticketamt

per3 = int(input("Enter age of person  3:"))
if(per3 < 12):
    price3 = ticketamt * 70 / 100
elif(per3 > 59):
    price3 = ticketamt * 50 / 100
else:
    price3 = ticketamt

per4 = int(input("Enter age of person  4:"))
if(per4 < 12):
    price4 = ticketamt * 70 / 100
elif(per4 > 59):
    price4 = ticketamt * 50 / 100
else:
    price4 = ticketamt

per5 = int(input("Enter age of person  5:"))
if(per5 < 12):
    price5 = ticketamt * 70 / 100
elif(per5 > 59):
    price5 = ticketamt * 50 / 100
else:
    price5 = ticketamt

print(f"ticket amount of person 1 = {price1}")
print(f"ticket amount of person 2 = {price2}")
print(f"ticket amount of person 3 = {price3}")
print(f"ticket amount of person 4 = {price4}")
print(f"ticket amount of person 5 = {price5}")
total = price1 + price2 + price3 + price4 + price5

print(f"Total ticket amount of 5 tickets = {total}")


