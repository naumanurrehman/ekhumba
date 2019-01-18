def recur(pre, curr, count, length):
    if count >= length:
        print(pre)
        return pre
    print(pre)
    return recur(curr, pre+curr, count+1, length)


def fibonacci(length):
    length = int(length)
    if length <= 0:
        return None
    if length == 1:
        print(length-1)
        return length-1
    if length == 2:
        print(length-2)
        print(length-1)
        return length-1
    return recur(0, 1, 1, length)


if __name__=='__main__':
    tests = [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (6, 5),
        (7, 8)
    ]

    for test in tests:
        print("Test: ", test[0])
        result = fibonacci(test[0])
        print("Result: ", result)
        if not result == test[1]:
            print("Error")
            print("Expected: ", test[1])
        else:
            print("Passed")
        print()

    while True:
        x = int(input("Enter index for list: "))
        print("Result: ", fibonacci(x))
        print()
