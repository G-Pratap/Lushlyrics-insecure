from threading import Thread
from time import sleep
videos = ['OOPs concept', 'Constructor', 'Destructor', 'File Handling']
class myThreadClass(Thread):
    # videos = ['OOPs concept', 'Constructor', 'Destructor', 'File Handling']
    def __init__(self):
        print("Constructor Called")
        Thread.__init__(self)
    def compression(self):
        print("Compression code executed")
    def run(self):
        self.compression()
        for vid in videos:
            print(f"{vid} started uploading")
            sleep(1)
            print(f"{vid} uploaded")

t1 = myThreadClass()
t1.start()      
sleep(5)
for i in range(5):
    print("Above code executed by thread-1")
    print("This is done by main Thread")

