product1 = float(input("Enter price of product 1:"))
product2 = float(input("Enter price of product 2:"))
product3 = float(input("Enter price of product 3:"))
product4 = float(input("Enter price of product 4:"))
product5 = float(input("Enter price of product 5:"))

total_cost = product1 + product2 + product3 + product4 + product5
print(f"Total cost of 5 products= Rs.{total_cost}")

Gst = total_cost * 18/100
total_bill = total_cost + Gst
print(f"18% GST= Rs.{Gst}")
print(f"Total bill with 18% GST= Rs.{total_bill}")