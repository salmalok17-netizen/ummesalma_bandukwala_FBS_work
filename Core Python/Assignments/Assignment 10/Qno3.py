# Write a program to find the second largest element in the list.

def secmaxEle(li):
    max = li[0]
    smax = 0
    for i in range(0, len(li)):
        if(max < li[i]):
            smax = max
            max = li[i]
        elif(smax < li[i]):
            smax = li[i]
    return smax

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
print(f"Second maximum element in the list is: {secmaxEle(li)}")