#Write a program to calculate area of rectangle

def areaRect(l,w):
    area = l * w
    return area

l = int(input("Enter length of rectangle:"))
w = int(input("Enter width of rectangle:"))
result = areaRect(l , w)
print(f"Area of rectangle is: {result}")

