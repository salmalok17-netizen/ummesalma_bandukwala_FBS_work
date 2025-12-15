# Python Program to Find the Second Largest Number in a List Using Bubble
# Sort

def bubbleSort(li):
    size = len(li)
    for i in range(1 , size):
        for j in range(0 , size - i):
            if(li[j] > li[j + 1]):
                li[j] , li[j + 1] = li[j + 1] , li[j]
    print(f"Sorted list is: {li}")
    return li[-2]      

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
result = bubbleSort(li)
print(f"The second largest element is: {result}")

