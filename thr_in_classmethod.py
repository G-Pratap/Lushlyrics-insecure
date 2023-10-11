from threading import Thread

class calc:
    def square(self, n):
        print(n*n)

    def cube(self, m):
        print(m*m*m)

e1=calc()
t1 = Thread(target=e1.square, args=(3,))
t2 = Thread(target=e1.cube, args=(4,))
t1.start()
t2.start()

for i in range(5):
    print('Square and Cube calculated successfully')
    