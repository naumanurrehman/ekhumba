#q = int(input("Enter number of queries: "))
s = input("Enter a string: ")

if s == s[::-1]:
    print("Entered string is a palindrome.")

else:
   # dL = list(s)    #Dummy List
    for i in range(len(s)):
        x = s[i]
        s = s[:i]+s[i+1:]
        #print(s)
        if s == s[::-1]:
            print("index: ", i, "character: ", x)
            break
        else:
            s = s[:i] + x + s[i:]

