#Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = float(input("Enter angle 1 of the triangle in degree:"))
angle2 = float(input("Enter angle 2 of the triangle in degree:"))
angle3 = float(input("Enter angle 3 of the triangle in degree:"))

tri = angle1 + angle2 + angle3
if(tri == 180):
    print(f"Triangle is valid")
else:
    print(f"Triangle is invalid")