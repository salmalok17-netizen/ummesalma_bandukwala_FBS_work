# Write a program to remove duplicates from the list.

def duplicate(li):
    li2 = []
    for i in range(0, len(li)):
        if li[i] not in li2:
            li2.append(li[i])
    return li2

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
result = duplicate(li)
print(f"List after removing duplicate elements is :{result}")
