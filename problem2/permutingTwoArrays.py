k = int(input("Enter integer k: "))
A = [1, 2, 2, 1]
B = [3, 3, 3, 4]

A.sort()
B.sort(reverse=True)
flag = 0
for i in range(len(A)):
    if A[i]+B[i] < k:
        flag = 1
        break

if flag == 1:
    print("No")
else:
    print("Yes")

