#Write a Python program to create a class using an object.Class and Object
class Student:
    def __init__(self,name,age,mark,course):
        self.name=name
        self.age=age
        self.mark=mark
        self.course=course
    
    def display(self):
        print("student details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mark:", self.mark)
        print("Course:", self.course)

s=Student("anu",22,45,"MCA")
s.display()

#Write a Python program using a constructor (__init__)  to initialize and display employee details.Constructor)
class Employee:
    def __init__(self,name,age,dept,salary):
        self.name=name
        self.age=age
        self.dept=dept
        self.salary=salary
    
    def show(self):
        print("Employee details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.dept)
        print("Salary:", self.salary)

emp=Employee("Deepak",22,"HR",45000)
emp.show()

#Write a Python program to demonstrate Single Inheritance using classes Animal and Dog .Single Inheritance
class Animal:
    def __init__(self,type):
        self.type=type
    def display(self):
        print("Animal Type and Sound")
class Dog(Animal):
    def __init__(self,type,breed):
        super().__init__(type)
        self.breed=breed
    def show(self):
        super().display()
        print("Type ",self.type)
        print("breed ",self.breed)
        print("sound bow bow")

d=Dog("Dog","german shepperd")
d.show()

#Write a Python program to demonstrate Multiple Inheritance using classes Father, Mother,Child. Multiple inheritance
class Father:
    def driving(self):
        print("Driving Skill")
class Mother:
    def cooking(self):
        print("Cooking Skill")
class Child(Father, Mother):
    def playing(self):
        super().cooking()
        super().driving()
        print("Playing Football")
c = Child()
c.playing()

#Write a Python program to demonstrate Multilevel Inheritance using classes A,B,C. MultiLevel inheritance
class A:
    def display(self):
        print("Class A method")
class B(A):
    def show(self):
        super().display()
        print("Class B  method")
class C(B):
    def get(self):
        super().show()
        print("Class C method")
b=B()
b.show()
c=C()
c.get()

#Write a Python program to demonstrate Polymorphism using classes Dog and Cat with the same method sound() .Polymorphism
class Dog:
    def sound(self):
        print("Dog Barks")
class Cat:
    def sound(self):
        print("cat meows")
d=Dog()
c=Cat()
d.sound()
c.sound()

#Write a Python program to demonstrate Method Overriding using parent and child classes.Runtime Polymorphism
class Parent:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("parent name",self.name)
class Child(Parent):
    def __init__(self,name,cname):
        super().__init__(name)
        self.cname=cname
    def show(self):
        print("child name",self.cname)
c=Child("arun","appu")
c.show()     

#Write a Python program to demonstrate Encapsulation using public and private variables.Encapsulation
class Animal:
    def __init__(self,name,breed,type):
        self.name=name
        self._breed=breed
        self.__type=type
    def show(self):
        print("name ",self.name)
        print("breed ",self._breed)
        print("type ",self.__type)
a=Animal("blacky","persian","cat")
a.show()
print(a.name)
print(a._breed)
print(a.__type)

#Write a Python program to create a BankAccount class with deposit and withdrawal methods.Class, Object, Methods)
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amt):
        self.amt=amt
        if self.amt>self.balance:
            print("insufficient balance")
        else:
            self.balance-=self.amt
            print("balance: ",self.balance)
    def deposit(self,amt):
        self.balance+=amt
        print("balance: ",self.balance)
b=BankAccount(5000)
b.deposit(2000)
b.withdraw(1000)

#Write a Python program to demonstrate Abstraction using an abstract class Shape and a subclass Square.Abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Square:", self.side * self.side)

s = Square(5)
s.area()

