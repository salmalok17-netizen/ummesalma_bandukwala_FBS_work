# Write a program to print all numbers which are divisible by m and n in the
# list.

def divisible(li,m,n):
    li2 = []
    for i in range(0, len(li)):
        if(li[i] % m == 0):
            if(li[i] % n == 0):
                li2.append(li[i])
    return li2

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
m = int(input("Enter value for m:"))
n = int(input("Enter value for n:"))
result = (divisible(li,m,n))
print(f"The elements divisible by {m} and {n} are : {result}")
