P = float(input("Enter principal amount:"))
T = float(input("Enter time period in years:"))
R = float(input("Enter rate of interest in %:"))

amount = P * ((1 + R/100) ** T)
compound_int = amount - P

print(f"The amount after {T}years is: {amount}")
print(f"The compound interest is: {compound_int}")