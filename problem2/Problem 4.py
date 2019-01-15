def check_pow_2(x):
    y = 2
    while y < x:
        y = y*2
    if y == x:
        print("Output: Yes and d is the power of 2")
    else:
        print("Output: No, d is not the power of 2")


n = int(input("Enter any integer: "))
d = int(input("Enter d: "))
if d*d == n:
    check_pow_2(d)
else:
    print("n is not the power of d")

