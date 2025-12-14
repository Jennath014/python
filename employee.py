class Person:
    def __init__(self, name, phno):
        self.name = name
        self.phno = phno

class Dept:
    def __init__(self, name, location):
        self.dname = name
        self.location = location

class Employee(Person, Dept):
    def __init__(self, name, phno, dname, location, desig, salary):
        Person.__init__(self, name, phno)
        Dept.__init__(self, dname, location)
        self.desig = desig
        self.salary = salary

    def show(self):
        print("Name:", self.name)
        print("Phone:", self.phno)
        print("Dept:", self.dname)
        print("Designation:", self.desig)
        print("Salary after increment:", self.salary * 1.10)

e = Employee("Rahul", "98765", "CS", "BLR", "Engineer", 30000)
e.show()
