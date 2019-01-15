n = int(input("Enter n: "))
x = 2
y = 2
x1 = 0
flag = False
''' Gives false at 2 and 3 because powers start from 2'''

if n == 1:
    print("Output: True\n" + str(n) + " can be expressed as " + str(1) + "^(0, 1, 2, 3, 4, 5, ......)")
else:
    while x <= n:
        #print(x)
        while x1 < n:
            x1 = x**y
         #print(x1)

            if x1 == n:
                print("Output: True\n" + str(n) + " can be expressed as " + str(x) + "^" + str(y))
                flag = True
                break
            y += 1

        y = 2
        x1 = 0
        x += 1
    if flag == False:
        print("Output: False")



