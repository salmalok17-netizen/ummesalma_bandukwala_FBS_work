#Write a program to input electricity unit charges and calculate total electricity bill
#according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

units = int(input("Enter units of electricity consumed:"))
billamt = 0

if(units > 0):
    if(units <= 50):
        billamt = units * 0.50

    elif(units <= 150):  # Next 100 units (51 to 150)
        billamt = (50 * 0.50) + ((units - 50) * 0.75)
    
    elif(units <= 250):  # Next 100 units (151 to 250)
        billamt = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)

    else:  # Units above 250
        billamt = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

print(f"Bill amount = {billamt}")
surcharge = billamt * 20 / 100
print(f"surcharge = {surcharge}")
total_bill = billamt + surcharge
print(f"Total bill = {total_bill}")
