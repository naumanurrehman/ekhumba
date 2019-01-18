def recur(char, state, seq):
    if char == '':
        return 0
    result = 0
    if state == 0:
        if not char == 'a':
            return 0
        state += 1
    elif state == 1:
        if char == 'b':
            state += 1
        elif char == 'c':
            return 0
    elif state == 2:
        if char == 'a':
            return 0
        elif char == 'c':
            state += 1
            result += 1
    elif state == 3:
        if not char == 'c':
            return 0
        result += 1
    num = len(seq)
    for loop in range(num):
        result += recur(seq[loop], state, seq[loop+1:])
    return result


def count_seq(content):
    result = 0
    size = len(content)
    for loop in range(size):
        result += recur(content[loop], 0, content[loop+1:])
    return result


if __name__ == '__main__':
    content = "abcc"
    res = count_seq(content)
    print(res)
