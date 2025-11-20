class Department:
    def __init__(self, dname,location):
        self.dname=dname
        self.location=location

    def display_d(self):
        print(f"Dept Name:{self.dname}")
        print(f"Location:{self.location}")


class Employee(Department):
    def __init__(self, dname,location,empid,ename,salary):
        super().__init__(dname,location)
        self.empid=empid
        self.ename=ename
        self.salary=salary

    def display_details(self):
        super().display_d()
        print(f"eid:{self.empid}")
        print(f"ename:{self.ename}")
        print(f"Salary:{self.salary}")

    def compare_salary(self, other_emp):
        if self.salary > other_emp.salary:
            print(f"{self.ename} higher salary than {other_emp.ename}")
        elif self.salary < other_emp.salary:
            print(f"{other_emp.ename}  higher salary than {self.ename}")
        



emp1 = Employee("CS", "MA", 101, "AMAL", 25000)
emp2 = Employee("IT", "MBITS", 102, "AVANTHIKA", 30000)
print("Employee 1:")
emp1.display_details()
print("Employee 2:")
emp2.display_details()
print("Salary Comparison:")
emp1.compare_salary(emp2)
