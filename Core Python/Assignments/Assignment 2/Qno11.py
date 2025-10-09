amt = float(input("Enter amount:"))
temp = amt

two_thousand = temp // 2000
temp = temp % 2000

five_hund = temp // 500
temp = temp % 500

two_hund = temp // 200
temp = temp % 200

hund = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

print(f"Denomination is: ")
print(f"2000/- = {two_thousand}") 
print(f"500/- = {five_hund}")
print(f"200/- = {two_hund}")
print(f"100/- = {hund}")
print(f"50/- = {fifty}")
print(f"20/- = {twenty}")
print(f"10/- = {ten}")

min_notes = two_thousand + five_hund + two_hund + hund + fifty + twenty + ten

print(f'Minimum no. of notes required for {amt} is {min_notes}')
