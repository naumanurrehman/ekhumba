s = input("Enter the string of numbers: ")
temp = []
flag = 0

j = [int(s[0]), int(s[:2])]
for x in j:
    for i in range(len(s)):
        temp.append(x)
        x += 1
        s1 = ''.join(str(e) for e in temp)
        if s1 == s:
            flag = 1
            break
    temp = []
    if flag == 1:
        print("String is a beautiful")
        break
else:
    print("String is ugly")


