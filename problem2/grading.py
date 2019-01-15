import array as arr
import math as m

n = int(input("Enter number of students : "))
while n > 60:
    print("Error (n > 60)! Enter again: ")
    n = int(input("Enter number of students : "))


ar = arr.array('i', [])
print("Enter grades: ")

for i in range(n):
    x = int(input())
    while x > 100:
        print("Error (grade > 100)! Enter again: ")
        x = int(input())
    ar.append(x)

for i in range(n):
    if ar[i] >= 38:
        if ar[i] % 5 >= 3:
            ar[i] = int(ar[i]/5)*5+5

print(ar)