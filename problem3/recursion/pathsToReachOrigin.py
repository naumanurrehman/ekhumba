def recur(x, y):
    if x == 0 or y == 0:
        return 1
    return recur(x-1, y) + recur(x, y-1)


def path_to_origin(x, y):
    if x == 0 and y == 0:
        return 0
    return recur(x, y)


if __name__=='__main__':
    tests = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 2),
        (1, 2, 3),
        (3, 1, 3),
        (3, 3, 20),
        (2, 4, 15),
        (4, 2, 15),
        (4, 3, 35)
    ]

    for test in tests:
        print("Test: ", test[0], ", ", test[1])
        result = path_to_origin(test[0], test[1])
        print("Result: ", result)
        if not result == test[2]:
            print("Error")
            print("Expected: ", test[2])
        else:
            print("Passed")
        print()

    while True:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        print(path_to_origin(x, y))
        print()
