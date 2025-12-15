# Write a program to create a new list from existing list which contains cube of
# each number of list.

def cube(li):
    li2 = []
    for i in range(0, len(li)):
        c = li[i] ** 3
        li2.append(c)
    return li2

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
result = cube(li)
print(f"The list with cube of each element is : {result}")

