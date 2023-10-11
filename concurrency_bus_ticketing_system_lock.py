from threading import Thread, current_thread, Lock
from time import sleep
mylock = Lock()
class Bus:
    def __init__(self, name, available_seats, mylock):
        self.name = name
        self.available_seats = available_seats
        self.mylock = mylock

    def reserve(self, required_seats):
        mylock.acquire()
        print(f"Available Seats are: {self.available_seats}")
        if self.available_seats >= required_seats:
            nm = current_thread().name
            print(f"{required_seats} are allocated to {nm}")
            self.available_seats-=required_seats
        else:
            print("Sorry! No seats available...")
        mylock.release()

b1 = Bus("Mahalakshmi_Travels", 20, mylock)
t1 = Thread(target=b1.reserve, args=(4,), name="Kapoor")
t2 = Thread(target=b1.reserve, args=(2,), name="Sharma")
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Remaining seats are {b1.available_seats}")