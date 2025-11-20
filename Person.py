class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __eq__(self,other):
        return self.__age == other.__age

    def __lt__(self,other):
        return self.__age < other.__age

    def __gt__(self,other):
        return self.__age > other.__age

p1= Person("Anu",20)
p2= Person("Deepu",30)

print(p1>p2)
print(p1==p2)
print(p1<p2)
