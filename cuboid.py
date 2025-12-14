class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

class Cuboid(Rectangle):
    def __init__(self, l, b, h):
        super().__init__(l, b)
        self.h = h

    def volume(self):
        return self.l * self.b * self.h

    def __le__(self, other):
        return self.volume() <= other.volume()

c1 = Cuboid(2, 3, 4)
c2 = Cuboid(3, 3, 3)

print(c1 <= c2)
