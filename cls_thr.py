import _thread
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "------------", time.time())

try:
    _thread.start_new_thread(print_epoch, ("thread 1", 2))
    _thread.start_new_thread(print_epoch, ("thread 2", 4))
except:
    print("There is an error!")
while 1:
    pass


