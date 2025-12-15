# Write a program to remove all occurrences of a given element in the list.

def removeEle(li,n):
    li2 = []
    for i in range(0, len(li)):
        if(li[i] != n):
            li2.append(li[i])
    return li2

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
n = int(input("Enter element you want to remove from list: "))
result = removeEle(li,n)
print(f"List after removing all occurances of given element is: {result}")