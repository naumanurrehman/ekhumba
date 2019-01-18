import time
import threading


def calc_sqr(ar):
    for i in ar:
        time.sleep(0.2)
        print("square:", i*i)


def calc_cube(ar):
    for i in ar:
        time.sleep(0.2)
        print("cube:", i*i*i)


ar = [2, 4, 8, 9]
t = time.time()
t1 = threading.Thread(target=calc_sqr, args=(ar,))
t2 = threading.Thread(target=calc_cube, args=(ar,))

t1.start()
t2.start()
t1.join()
t2.join()

print("done in", time.time()-t)



