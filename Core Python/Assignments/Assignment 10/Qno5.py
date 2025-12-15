# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def checkEle(li, n):
    for i in range(0 , len(li)):
        if n in li:
            return print(f"{n} is present in the list {countOccurrence(li,n)} times.")
        else:
            return print(f"{n} is not present in the list.")

def countOccurrence(list, n):
    count=0
    for i in list:
        if(i==n):
            count=count+1
    return count
   
li = [22, 32,42,22,23,43,11,39,22]
n = int(input("Enter number you want to search:"))
ele = checkEle(li,n)
# result = countOccurrence(li,n)
# print(f"The number is present {result} times.")
