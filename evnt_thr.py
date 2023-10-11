import threading
import time
e = threading.Event()

def task():
    print("game is started")
    time.sleep(5)
    e.set()


def end():
    e.wait()
    if e.is_set():
        print("code for destroying the session")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)

t1.start()
t2.start()