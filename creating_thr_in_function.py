from threading import Thread, current_thread

def display(n, msg):
    for i in range(n):
        print(msg, current_thread())

t1 = Thread(target=display, args=(5, "Welcome to Threading"))
t1.start()

for i in range(5):
    print("Welcome")