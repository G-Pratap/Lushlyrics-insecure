import threading
import time

def square(num):
    print("Square={}".format(num*num))

def cube(num):
    print("Cube={}".format(num*num*num))


if __name__ == "__main__":
    t1 = threading.Thread(target=square, args=(2,))
    t2 = threading.Thread(target=cube, args=(2,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Done")

    