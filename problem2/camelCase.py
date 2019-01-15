s = input("Enter the string : ")

UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 1
for i in s:
    if UC.find(i) != -1:
        count += 1

print(count)