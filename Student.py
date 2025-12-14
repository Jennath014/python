class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class Marks:
    def __init__(self, maths, comp):
        self.maths = maths
        self.comp = comp

class Student(Person, Marks):
    def __init__(self, name, roll, maths, comp):
        Person.__init__(self, name, roll)
        Marks.__init__(self, maths, comp)

    def show(self):
        total = (self.maths + self.comp) / 2
        print(self.name, self.roll)
        print("Pass" if total >= 50 else "Fail")

s = Student("Asha", 10, 55, 45)
s.show()
