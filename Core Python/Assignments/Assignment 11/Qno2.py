# Python Program to Merge Two Lists and Sort it

def merge(li1,li2):
    li1.extend(li2)
    li3 = li1
    return li3

def sort(li):
    size = len(li)
    for i in range(1 , size):
        for j in range(0 , size - i):
            if(li[j] > li[j + 1]):
                li[j] , li[j + 1] = li[j + 1] , li[j]
    return li

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

result = merge(li,li2)
print(f"Merged list is: {result}")
sorted = sort(result)
print(f"Sorted list is: {sorted}")