n = 2**int(input())

count = 0
temp = 10


x = 1
while x:
    count = count+1
    if n<temp:
        x = 0
    temp = temp * 10

print('The number of digits are: ', count)

