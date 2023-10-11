class Employee:
    raise_amt = 1.05

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + "." + lastname + "@gmail.com"
        self.pay = pay

    def fullname(self):
        return print(f"{self.firstname} {self.lastname}")
    
    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # return (self.pay)
    
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, firstname, lastname, pay, employees=None):
        super().__init__(firstname, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmployee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remEmployee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmployee(self):
        for emp in self.employees:
            print(emp.fullname(), emp.email)


dev1 = Developer("Rama", "Sudhakar", 50000, "Python")
dev2 = Developer("Sharman", "Joshi", 60000, "Java")

mgr1 = Manager("Gulshan", "Kumar", 90000, [dev1, dev2])

# print(dev1.prog_lang)
mgr1.printEmployee()
# print(mgr1.email)
mgr1.remEmployee(dev1)
# mgr1.printEmployee()
mgr1.remEmployee(dev2)
mgr1.addEmployee(dev1)
mgr1.printEmployee()