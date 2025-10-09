print("Enter distant in feet and inches")
feet =  int(input("Feet:"))
inches = int(input("Inches:"))

total_inches = (feet * 12) + inches
total_centi = total_inches * 2.54

meters = int(total_centi // 100)
centi = (total_centi % 100)

print(f"{feet}feet and {inches}inches = {meters}meters and {centi}centimeters")
