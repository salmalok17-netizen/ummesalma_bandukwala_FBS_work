sub1 = int(input("enter marks for subject 1:"))
sub2 = int(input("enter marks for subject 2:"))
sub3 = int(input("enter marks for subject 3:"))
sub4 = int(input("enter marks for subject 4:"))
sub5 = int(input("enter marks for subject 5:"))

obtained_marks = sub1+sub2+sub3+sub4+sub5
total_marks = 500
percentage = (obtained_marks / total_marks) * 100

print (f'Total marks obtained: {obtained_marks}')
print (f"Percentage is: {percentage}%")

       