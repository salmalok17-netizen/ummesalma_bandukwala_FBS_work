#Write a program to input all sides of a triangle and check whether triangle is valid or
#not.

side1 = float(input("Enter side 1 of the triangle:"))
side2 = float(input("Enter side 2 of the triangle:"))
side3 = float(input("Enter side 3 of the triangle:"))

if(side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print(f"Triangle is valid")
else:
    print(f"Triangle is invalid")