#         1   
#       1   2
#     1       3   
#   1           4
# 1   2   3   4   5

for i in range(1, 6):
    for j in range(5- i):
        print(" ", end = " ")

    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print(j, end = " ")
            print(end = "  ")
        else:
            print("   ", end = " ")
    print()