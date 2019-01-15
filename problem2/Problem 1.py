n = 2**int(input("Enter n: "))
count = 0;

while n >= 1:
    n /= 10
    count += 1

print(count)
