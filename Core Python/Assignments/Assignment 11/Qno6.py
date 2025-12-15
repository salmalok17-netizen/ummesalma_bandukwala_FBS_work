# Python Program to Find the Union of two Lists

def getUnion(li1, li2):
    unionli = []
    for ele in li1:
        if ele not in unionli:
            unionli.append(ele)

    for ele in li2:
        if ele not in unionli:
            unionli.append(ele)

    return unionli

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
result = getUnion(li, li2)
print("The union of the two lists is:", result)