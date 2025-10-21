#Write a program to check whether the triangle is equilateral, isosceles or scalene
#triangle.

side1 = float(input("Enter side 1 of the triangle:"))
side2 = float(input("Enter side 2 of the triangle:"))
side3 = float(input("Enter side 3 of the triangle:"))

if(side1 == side2) and (side2 == side3):
    print(f"It is an Equilateral triangle")
elif(side1 == side2) or (side1 == side3) or (side2 == side3):
    print(f"It is an Isosceles triangle")
else:
    print(f"It is a Scalene triangle")
