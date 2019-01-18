import array as arr
n = 5

ar = arr.array('i', [])
print("Enter elements: ")

for i in range(n):
    ar.append(int(input()))

print(ar)

s1 = 0
s2 = 0

for j in range(4):
    mx = ar[0]

    for i in range(len(ar)):
        if mx < ar[i]:
            mx = ar[i]

    s1 = s1 + mx
    ar.remove(mx)
    if j == 0:
        s2 = sum(ar)
print(s2, s1)

