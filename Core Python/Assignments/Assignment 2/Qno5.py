cost_price = float(input("Enter cost price of the book:"))
disc_per = float(input("Enter the discount percentage:"))

disc_amt = cost_price * (disc_per / 100)
selling_price = cost_price - disc_amt

print(f"Cost price: {cost_price}")
print(f"Discount: {disc_per}%")
print(f"Selling price: {selling_price}")