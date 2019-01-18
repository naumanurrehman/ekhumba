import array as arr
t = int(input("Enter no. of test cases : "))

n = arr.array('i', [])
print("Enter the integers : ")

for i in range(t):
    n.append(int(input()))

for i in range(t):
    count = 0
    temp = n[i]
    while temp > 0:
        r = temp % 10
        #print(r)
        if r != 0:
            if n[i] % r == 0:
                count += 1
        temp = int(temp / 10)
        #print(temp)

    print(count)

