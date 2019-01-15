n = int(input("Enter n: "))
x = int(input("Enter x: "))
power = 0
z = 0
st = ""

while n >= 1:
    while x**power <= n:
        power += 1

    z = power - 1
    n = n - x**z
    st = "+" + str(x) + "^" + str(z) + st
    power = 0

print(st)
