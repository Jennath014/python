class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name : {self.name} ")
        print(f"Age : {self.age} ")

class Employee(Person):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.EmpID=eid

    def display(self):
        super().display()
        print(f"Employee id: {self.EmpID} ")

class Faculty(Employee):
    def __init__(self,name,age,eid,dep):
        super().__init__(name,age,eid)
        self.department=dep

    def display(self):
        super().display()
        print(f"Department: {self.department} ")

class Researcher:
    def can_do_research(self):
        print( "This person can conduct research")


class Professor(Faculty,Researcher):
    def __init__(self,name,age,eid,dep):
        Faculty.__init__(self,name,age,eid,dep)

        
p= Professor("Victor Frankestein ",38,'E001', 'Biology')
p.display()
p.can_do_research()

