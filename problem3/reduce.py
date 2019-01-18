def func(x, y, z):
    return x+y+z

seq = [1, 2, 3, 4, 5, 6]
print(reduce(func, seq))

