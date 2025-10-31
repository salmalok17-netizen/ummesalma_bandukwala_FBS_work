# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n = int(input("Enter number of student's percentage to be calculated:"))
total_percent = 0

for i in range(1, n+1):
    print(f"Enter marks for student: {i}")
    sub1 = float(input("Subject 1: "))
    sub2 = float(input("Subject 2: "))
    sub3 = float(input("Subject 3: "))
    sub4 = float(input("Subject 4: "))
    sub5 = float(input("Subject 5: "))

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percent = total / 500 * 100

    print(f"Percentage of student {i} is: {percent}")
    print()
    total_percent = total_percent + percent

avg = total_percent / n
print(f"Average percentage of students is: {avg}")


        
