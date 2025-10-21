#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))
sub5 = float(input("Enter marks of subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percent = total / 500 * 100
print(f"Percentage = {percent}")

if(percent >= 70):
    print(f"Grade: First Class with Distinction")

elif(percent >= 60 and percent < 70):
    print(f"Grade: First Class")

elif(percent >= 55 and percent < 60):
    print(f"Grade: Upper Second Class")

elif(percent >= 50 and percent < 54):
    print(f"Grade: Lower Second Class")

elif(percent >= 40 and percent < 50):
    print(f"Grade: Pass Class")

else:
    print("Grade: Fail")