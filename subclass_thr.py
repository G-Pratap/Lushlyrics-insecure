# from threading import Thread
# from time import sleep

# class mycustomthread(Thread):
#     def __init__(self, thread_name, thread_Id):
#         Thread.__init__(self)
#         self.thread_name = thread_name
#         self.thread_Id = thread_Id
#     def run(self):
#         print("Starting--:" + self.thread_name)
#         for i in range(3):
#             print("Good Morning!!")
#             # sleep(3)
#         for i in range(3):
#             print("Good Afternoon!!")
#             # sleep(3)
#         print("Exiting--:" + self.thread_name)
#     def cube(self, num):
#         Cube = num*num*num
#         print (Cube)
#     def square(self, num):
#         square = num*num
#         print (square)
# t1 = mycustomthread("Thread1", 1000)
# t2 = mycustomthread("Thread2", 2000)
# t1.cube(2)
# t2.square(3)
# t1.start()
# sleep(2)
# t2.start()
# print("Good Night!!")


from threading import Thread
from time import sleep

class mycustomthread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(3):
            print("Good Morning!!")
            # sleep(3)
        self.cube(3)
        self.square(2)
        for i in range(3):
            print("Good Afternoon!!")
            # sleep(3)
    def cube(self, num):
        Cube = num*num*num
        print (Cube)
    def square(self, num):
        square = num*num
        print (square)


t1=mycustomthread()
t1.start()
print("Good Night!!")