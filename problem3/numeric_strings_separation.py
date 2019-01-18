def numeric_separation(num_str):
    if len(num_str) < 2:
        return []

    count = 1
    result = []
    x = num_str[0]
    y = num_str[1]
    while count < len(num_str):
        count = count + 1
        diff = int(x) - (int(y)-1)
        if diff == 0:
            result.append(x)
            if count < len(num_str):
                x = y
                y = num_str[count]
                continue
            else:
                break
        if count >= len(num_str):
            return []
        if diff > 0:
            y += num_str[count]
        else:
            x += num_str[count-len(y)]
            y = y[1:] + num_str[count]
    result.append(y)
    return result


if __name__ == '__main__':
    print("Numeric String separation")
    tests = [
        ("", []),
        ("8", []),
        ("89", ["8", "9"]),
        ("99100", ["99", "100"]),
        ("991001", []),
        ("9899100", ["98", "99", "100"]),
        ("9899101", []),
        ("891011", ["8", "9", "10", "11"]),
        ("123124", ["123", "124"])
    ]
    for test in tests:
        result = numeric_separation(test[0])
        if result != test[1]:
            print("Failed for test: "+test[0])
            print("Returned: "+",".join(result))
            print("Instead of: "+",".join(test[1]))
            exit(1)
    print("All test passed successfully")
    while True:
        str = input("Please enter any numeric string: ")
        res = numeric_separation(str)
        print("Result: "+",".join(res))
