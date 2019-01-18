def func(num):
    return 2*num


x = [1, 2, 3, 5, 4]
r = list(map(func, x))
print(r)
