s = input("Enter the string of numbers: ")
temp = []
flag = 0

x = int(s[0])

for i in range(len(s)):
    temp.append(x)
    x += 1
    s1 = ''.join(str(e) for e in temp)
    if s1 == s:
        flag = 1
        break

if flag == 1:
    print("String is a beautiful")
else:
    print("String is ugly")


