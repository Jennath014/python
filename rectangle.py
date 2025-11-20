class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)

    def area(self):
        return self.length*self.breadth

    def compare(self,other):
        if self.area() != other.area():
            print("area different")

        else:
            print("Area same")

r1=Rectangle(2,5)
r2=Rectangle(2,3)
print("area of r1:",r1.area())
print("area of r2:",r2.area())
print("perimeter of r1:",r1.perimeter())
print("perimeter of r2:",r2.perimeter())
r1.compare(r2)


