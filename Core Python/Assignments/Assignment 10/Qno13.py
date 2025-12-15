# Write a program to print list after removing even numbers.

def removeEven(li):
    li2 = []
    for i in range(0, len(li)):
        if(li[i] % 2 != 0):
            li2.append(li[i])
    return li2

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
result = removeEven(li)
print(f"The list after removing even numbers is: {result}")
