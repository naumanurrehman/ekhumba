import array as arr

n = int(input("Enter the size of the array: "))

ar = arr.array('i', [])
print("Enter elements: ")

for i in range(n):
    ar.append(int(input()))

s = sum(ar)
print(s)


'''s = 0   #sum
for i in range(n):
    s = s + ar[i]

print(s)
'''

