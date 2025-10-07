total_days = int(input("Enter number of days:"))

years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7

print(f"{total_days} days is equivalent to:")
print(f"Years: {years}")
print(f"Weeks: {weeks}")
print(f"Days: {remaining_days}")
