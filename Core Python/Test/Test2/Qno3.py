r = 20
l = 50
b = 40
barbed_wire = 35

peri_of_rect = (2 * l) + b
circum_of_semicircle = 3.14 * r

peri_of_field = peri_of_rect + circum_of_semicircle
print(f"Perimeter of field= {peri_of_field}mtrs")

one_time = peri_of_field * barbed_wire
total_cost = one_time * 5

print(f"one fence of barbed wire= Rs.{one_time}")
print(f"Total cost of fencing= Rs.{total_cost}")