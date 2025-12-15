# Write a program to reverse the list.

def reverse(li):
    li2=[]
    for i in range(len(li)-1 ,-1, -1):
        li2.append(li[i])
    return li2

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
result = (reverse(li))
print(f"The reversed list is: {result} ")