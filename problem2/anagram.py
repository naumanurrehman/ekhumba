s = input("Enter a string: ")

s1, s2 = s[:int(len(s)/2)], s[int(len(s)/2):]

count = 0

for j in s2:
    if s1.find(j) < 0:
        count += 1

print(count)