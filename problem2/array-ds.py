import array as arr

n = int(input("Enter the number of elements of the array: "))

ar = arr.array('i', [])
ar_rev = arr.array('i', [])

print("Enter elements: ")

for i in range(n):
    #print(i)
    ar.append(int(input()))

for i in range(int(n/2)):
    a = ar[i]
    ar[i] = ar[n-1-i]
    ar[n-i-1] = a


#ar_rev = ar[::-1]

print(ar)
