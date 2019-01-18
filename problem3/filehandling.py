with open('hello.txt', 'a+') as file:
    file.seek(0)
    lines = file.readlines()
    for line in lines:
        print(line)
    file.write('Hello')
