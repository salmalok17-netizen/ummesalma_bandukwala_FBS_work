# Write a program to find sum of all elements of list

def sumOfEle(li):
    sum = 0
    for i in range(0, len(li)):
        sum = sum + li[i]
    return sum
    
count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
result = (sumOfEle(li))
print(f"The sum of list  is {result}")