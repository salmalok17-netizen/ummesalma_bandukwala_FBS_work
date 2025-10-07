lenght = float(input("Enter lenght of the rectangle:"))
breadth = float(input("Enter breadth of the rectangle:"))
radius = float(input("Enter radius of the circle:"))

area_of_rect = lenght * breadth
#area_of_circle = 3.14 * radius**2
area_of_semicircle = (3.14 * radius**2) / 2

print(f"Area of rectangle is {area_of_rect}")
#print(f"Area of circle is {area_of_circle}")
print(f"Area of semicircle is {area_of_semicircle}")

area_of_stadium = area_of_rect + area_of_semicircle

peri_of_rect = 2 * (lenght + breadth)
peri_of_semicircle = radius * (3.14 + 2)

print(f"Perimeter of rectangle is {peri_of_rect}")
print(f"Perimeter of semicircle is {peri_of_semicircle}")

peri_of_stadium = peri_of_rect + peri_of_semicircle

print(f"Area of the given figure is: {area_of_stadium}")
print(f"Perimeter of the given figure is: {peri_of_stadium}")