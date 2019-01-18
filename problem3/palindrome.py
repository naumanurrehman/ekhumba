def palindrome(s):
    if s == s[::-1]:
        return []
    for i in range(len(s)):
        x = s[i]
        s = s[:i] + s[i + 1:]
        # print(s)
        if s == s[::-1]:
            return i
        else:
            s = s[:i] + x + s[i:]
    return False

q = int(input("Enter number of queries: "))

strs = []
indeces = []
for i in range(q):
    strs.append(input("Enter string: "))
for str in strs:
    indeces.append(palindrome(str))

print(indeces)
