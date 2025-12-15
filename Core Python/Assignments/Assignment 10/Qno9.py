# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

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
