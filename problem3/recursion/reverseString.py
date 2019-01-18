'''
Given a string, Write recursive function that reverses the string.

Input Format

A String.

Constraints

x

Output Format

Reverse of Strings.

Sample Input

Being

Sample Output

gnieB

Explanation

Self explanatory.
'''


def recur(content, num, length):
    if num >= length:
        return ''
    return recur(content, num+1, length) + content[num]


def reverse_string(content):
    return recur(content, 0, len(content))


if __name__ == '__main__':
    tests = [
        ("Yello", "olleY"),
        ("King", "gniK"),
        ("", ""),
        ("Nauman", "namuaN"),
        ("a", "a")
        ]

    for test in tests:
        print("Test: ", test[0])
        result = reverse_string(test[0])
        print("Result: ", result)
        if not result==test[1]:
            print("Error")
            print("Expected: ", test[1])
        else:
            print("Passed")
        print()

    while True:
        content = input("Enter a string: ")
        print(reverse_string(content))
        print()
