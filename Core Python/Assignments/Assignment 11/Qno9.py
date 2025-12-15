# Write a program to create three lists of numbers, their squares and cubes

def sqrCube(li):
    num = []
    sqr = []
    cube = []
    for i in range(0, len(li)):
        num.append(li[i])
        s = li[i] ** 2
        sqr.append(s)
        c = li[i] ** 3
        cube.append(c)
    return num,sqr,cube

count = int(input("Enter number of elements you want in the list:"))
li = []
for i in range(1 , count + 1):
    ele = int(input(f"Enter value {i}:"))
    li.append(ele)
num,sqr,cube = sqrCube(li)
print("Three lists of number, their square and cube are:")
print(f"number: {num}")
print(f"square: {sqr}")
print(f"cube: {cube}")
