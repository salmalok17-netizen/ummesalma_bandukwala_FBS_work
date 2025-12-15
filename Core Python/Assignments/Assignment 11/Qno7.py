# Python Program to Find the Intersection of Two Lists

def intersect(li1,li2):
    intersectli = []
    for ele in li1:
        if ele in li2 and ele not in intersectli:
            intersectli.append(ele)
    return intersectli

count = int(input("Enter number of elements you want in the list 1:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)

count2 = int(input("Enter number of elements you want in the list 2:"))
li2 = []
for i in range(1 , count2 + 1):
    ele = int(input(f"Enter value {i}:"))
    li2.append(ele)
print(li2)

result = intersect(li,li2)
print(f"Intersection of both list is: {result}")