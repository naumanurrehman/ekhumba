def arrsum(arr=[]):
    return sum(arr)


n=int(input('Enter num of elements in array'))
arr=[]
for x in range(n):
    z=int(input())
    arr.append(z)

print(arrsum(arr))