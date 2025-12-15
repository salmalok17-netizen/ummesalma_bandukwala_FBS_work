# Write a program to create a duplicate of an existing list. It should not point to
# same list.

def duplicateList(li):
    li2 = []
    for i in range(0, len(li)):
        li2.append(li[i])
    return li2

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
result = duplicateList(li)
print(f"The duplicate list is : {result}")
# print(id(li))
# print(id(result))