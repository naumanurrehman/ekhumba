import array as arr
inp = input("Enter n and k: ").split()
n = int(inp[0])
k = int(inp[1])

ar = arr.array('i', [])
print("Enter the integers : ")

for i in range(n):
    ar.append(int(input()))

count = 0

for i in range(n):
    j = i + 1
    while j < n:
            if (ar[i] + ar[j]) % k == 0:
                count += 1
            j += 1
print(count)
