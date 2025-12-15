# Python Program to Put Even and Odd elements of a List into two Different
# Lists

def evenOdd(li):
    even = []
    odd = []
    for i in range(0, len(li)):
        if(li[i] % 2 == 0):
            even.append(li[i])
        else:
            odd.append(li[i])
    return even,odd

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
print(li)
even,odd = (evenOdd(li))
print(f"The even and odd lists are:")
print(f"Even list: {even}")
print(f"Odd list: {odd}")