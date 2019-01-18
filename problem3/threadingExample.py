import threading


def find_cube(val):
    for num in range(val):
        print('Cube of ', num, ': ', num*num*num)


def find_square(val):
    for num in range(val):
        print('Square of ', num, ': ', num*num)


if __name__ == '__main__':
    number = 1000
    t1 = threading.Thread(target=find_cube, args=(number, ))
    t2 = threading.Thread(target=find_square, args=(number, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
