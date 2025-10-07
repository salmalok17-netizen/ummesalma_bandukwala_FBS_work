a = float(input("Enter coefficient 'a':"))
b = float(input("Enter coefficient 'b':"))
c = float(input("Enter coefficient 'c':"))

discriminant = (b**2 - 4*a*c)**0.5
root1= (-b + discriminant) / 2 *a
root2= (-b - discriminant) / 2 *a

print(f"The roots are: {root1} & {root2}")

 