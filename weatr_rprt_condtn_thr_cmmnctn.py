import threading
import time

def write_data():
    con.acquire()
    with open('report.txt', 'w', encoding="utf-8") as file1:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']
        for i in days:
            temp = input(f"Enter the temperature for {i}")
            file1.write(temp+"\n")
    con.notify_all()
    con.release()

def max_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt', 'r', encoding="utf-8") as file1:
        data = file1.readlines()
        max1 = float(data[0].strip("\n"))
        for temp in data[1:]:
            temp = float(temp.strip("\n"))
            if temp > max1:
                max1=temp
        print("Maximum temp. is: ", max1)
    # with open('report.txt', 'w') as file1:
    #     file1.write("Maximum temperature is {max1}")
        con.release()

def avg_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt', 'r', encoding="utf-8") as file1:
        data = file1.readlines()
        tot = 0
        for temp in data:
            temp = float(temp.strip("\n"))
            tot += temp
        avg = tot // 7
        print(tot)
        print("Average temp. is: ", avg)
    # with open('report.txt', 'w') as file1:
    #     file1.write("Avg temperature is {avg}")
        con.release()

con = threading.Condition()
t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.start()
t2.start()
t3.start()
