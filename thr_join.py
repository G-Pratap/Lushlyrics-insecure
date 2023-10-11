from threading import Thread
import time

def upload():
    print("Uploading starts")
    time.sleep(3)
    print("Video uploaded")

def notifications():
    print("Sending notifications to Subscribers")

t1 = Thread(target=upload)
t2 = Thread(target=notifications)
t1.start()
t1.join()
t2.start()
t2.join()

for i in range(4):
    print("Hello")
