def power(n,d):
    p=0
    temp=pow(d,p)
    while(temp<=n):
        if temp is n:
            return 1
        p=p+1
        temp=pow(d,p)
    return 0

print(power(64,8))