class A:
    def display(self):
        print("This method belongs to Class A")

class B(A):
    def display(self):
        print("This method belongs to Class B")

b1 = A()
b2 = B()
b1.display()
b2.display()