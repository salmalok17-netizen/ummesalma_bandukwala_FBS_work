#         1   
#       1   1   
#     1   2   1
#   1   3   3   1

for i in range(4):  
    num = 1
    for j in range(4 - i):  # Inner loop for spaces
        print(" ", end=" ")

    for j in range(i + 1):  # Inner loop for numbers
        print(num, end="   ")
        num = num * (i - j) // (j + 1)  
    print()

