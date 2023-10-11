class Employee:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def fullname(self):
        print(self.fname + " " + self.lname)

e1 = Employee('Gaorav', 'Pratap', 23)
e2 = Employee('Ram', 'Sudama', 24)

e1.fullname()
e2.fullname()
