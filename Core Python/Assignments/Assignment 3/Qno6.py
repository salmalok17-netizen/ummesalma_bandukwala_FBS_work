#Write a program to calculate profit or loss.

cost_price = float(input("Enter cost price of the product:"))
sell_price = float(input("Enter selling price of the product:"))

if(sell_price > cost_price):
    profit = sell_price - cost_price
    print(f"Profit = Rs.{profit}")

elif(cost_price > sell_price):
    loss = cost_price - sell_price
    print(f"Loss = Rs.{loss}")
    
else:
    print(f"No profit no loss")
