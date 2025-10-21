area_of_onewall = float(input("Enter area of one wall:"))
int_cost = float(input("Enter interior cost of the painting:"))
ext_cost = float(input("Enter exterioir cost of the painting:"))

area_int = area_of_onewall * 8
area_ext = area_of_onewall * 7

interior_cost = int_cost * area_int
exterioir_cost = ext_cost * area_ext

print(f"Cost of Interior walls is : Rs.{interior_cost} ")
print(f"Cost of Exterioir walls is : Rs.{exterioir_cost}")

