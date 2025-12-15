#Write a program to calculate area of circle

def areaCircle(r):
    area = 3.14 * r**2
    return area

r = int(input("Enter radius of circle:"))
result = areaCircle(r)
print(f"Area of circle is: {result}")