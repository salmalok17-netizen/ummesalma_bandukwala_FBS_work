# Print 1 to 100 in snakes and ladder pattern.

li = []
for i in range(9, -1, -1):
    sub_li = []
    for j in range(i * 10 + 1, (i * 10 + 1) + 10,): #((i + 1) * 10 + 1)
        #sub_li.append()
        sub_li = sub_li + [j]
    if(i % 2 != 0):
        sub_li.reverse()
    #li.append(sub_li)
    li = li + [sub_li]

for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j], end = " ")
    print()
   