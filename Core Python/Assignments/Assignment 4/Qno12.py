# WAP to print Armstrong number within a given range

start = int(input("Enter number from you want to print armstrong number:"))
end = int(input("Enter number till you want to print armstrong number:"))

for i in range(start, end + 1):
    power = (len(str(i)))
    sum = 0
    temp = i
    while(temp > 0):
        d = temp % 10
        sum = sum + d ** power
        temp = temp // 10
    if(i == sum):
        print(i)
        