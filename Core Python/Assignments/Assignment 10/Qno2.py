# Write a program to find maximum and minimum element in a list.

def maxEle(li):
    max = li[0]
    for i in range(0, len(li)):
        if(max < li[i]):
            max = li[i]
    return max

def minEle(li):
    min = li[0]
    for i in range(0, len(li)):
        if(min > li[i]):
            min = li[i]
    return min

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
print(f"Maximum element is: {maxEle(li)}")
print(f"Minimum element is: {minEle(li)}")

