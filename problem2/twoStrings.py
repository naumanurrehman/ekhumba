n = int(input("No. of test cases: "))
for k in range(n):
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    #st = ""
    flag = 0
    for i in s1:
        #print("i: " + i)
        for j in s2:
            #print("j: " + j)
            if i == j:
                #st = st + i
                print("Yes")
                flag = 1
                break
        if i == j:
            break


    if flag == 0:
        print("No")
    #else:
        #print("Yes")
        # print("Common substring is: " + st)
