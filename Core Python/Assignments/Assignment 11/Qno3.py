# Python Program to Sort the List According to the Second Element in Sublist

def sort(li):
    size = len(li)
    for i in range(1 , size):
        for j in range(0 , size - i):
            if(li[j][1] > li[j + 1][1]):
                li[j] , li[j + 1] = li[j + 1] , li[j]
    return li

# li = [[2,4] , [3,5] , [2,2] , [7,1] , [8,3]]
count = int(input("Enter number of elements you want in the list:"))
li = []
subli= []
for i in range(1 , count + 1):
    for j in range(1 , 3):
        ele = int(input(f"Enter value {j} for sublist{i}:"))
        subli.append(ele)
    li.append(subli)
    subli = []
print(f"The list is: {li}")
result = sort(li)
print(f"The list after sorting according to the second element in sublist is: {result}")