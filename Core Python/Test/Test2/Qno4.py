side = int(input("Enter size of a wall:"))
cost_of_paint = float(input("Enter interior cost of paint of building:"))

area_of_building = side**2
print(f"Area of building is= {area_of_building}")

total_cost = area_of_building * cost_of_paint
print(f"Total cost of painting is= Rs.{total_cost}")