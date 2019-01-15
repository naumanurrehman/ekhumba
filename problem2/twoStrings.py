n = int(input("No. of test cases: "))
for k in range(n):
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    flag = 0
    for i in s1:
        if s2.find(i) > 0:
            print("Yes")
            flag = 1
            break

    if flag == 0:
        print("No")

