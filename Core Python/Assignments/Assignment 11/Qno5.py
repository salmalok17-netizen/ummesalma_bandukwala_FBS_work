# Python Program to Sort a List According to the Length of the Elements
# within the list.

def sortByLen(li):
    size = len(li)
    for i in range(size):
        for j in range(0 , (size - i) - 1):
            if len(li[j]) > len(li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]
    return li

li = ["apple", "banana", "cherry", "date", "fig"]
print(li)
sorted_list = sortByLen(li)
print(f"The sorted list is: {sorted_list}")