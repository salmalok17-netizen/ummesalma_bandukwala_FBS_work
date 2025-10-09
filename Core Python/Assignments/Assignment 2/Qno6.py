basic_salary = float(input("Enter basic salary of the employee:"))

da= basic_salary * 10 / 100
ta = basic_salary * 12 / 100
hra =basic_salary * 15 / 100

print(f"da = {da}")
print(f"fa = {ta}")
print(f"hra = {hra}")

total_sal = basic_salary + da + ta + hra
print(f"Total salary of the employee is = {total_sal}/-")
