import threading
import time
e = threading.Event()

def signal():
    while True:
        print("Light is Green")
        e.set()
        time.sleep(5)
        print("Light is Red")
        e.clear()
        time.sleep(5)
        e.set()
     

def msg():
    e.wait()
    while e.is_set():
        print("You Can GO!")
        time.sleep(0.5)
        e.wait()


t1 = threading.Thread(target=signal)
t2 = threading.Thread(target=msg)

t1.start()
t2.start()