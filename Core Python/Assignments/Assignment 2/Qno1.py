hrs = int(input("Enter hours:"))
mins = int(input("Enter minutes:"))
secs = int(input("Enter seconds"))

print(f"time entered is= {hrs}: {mins}: {secs}")

total_secs = (hrs * 3600) + (mins * 60) + secs

print(f"total seconds of {hrs}hrs : {mins}mins : {secs}sec is {total_secs}seconds")