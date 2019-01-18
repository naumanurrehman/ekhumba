import array as arr
import math as m
n = int(input("Enter size of array : "))

arr = input("Enter array : ").split()

#ar = arr.array('i', [])
#print("Enter elements: ")

#for i in range(n):
#    ar.append(int(input()))

arr.sort()
print(arr[m.floor(n/2)])
