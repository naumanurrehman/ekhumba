def odd(num):
    return num % 2


seq = [1, 2, 5, 7, 8, 4]
print(list(filter(odd, seq)))