import math
def powerfun(num):
    from math import sqrt

    for x in range(int(sqrt(num))):
        for y in range(x):
            temp=pow(y,x)
            if temp is num:
                return 1

    return 0

num=3410075
print(powerfun(num))

