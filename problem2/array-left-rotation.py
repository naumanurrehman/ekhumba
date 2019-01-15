import array as arr
st = input("Enter n and d : ").split()

n = int(st[0])
d = int(st[1])

ar = arr.array('i', [])
print("Enter elements: ")

for i in range(n):
    ar.append(int(input()))

for i in range(d):

    first = ar[0]
    for j in range(n-1):
        ar[j] = ar[j+1]
    ar[n-1] = first

print(ar)