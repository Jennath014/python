"'create class Engine (_power) and wheels (_size). Derive the class Car (_model) from engine & wheels . display details  of the car using  method overriding'"

class Engine:
    def __init__(self,power):
        self._power=power

    def show(self):
        print(f"Engine power: {self._power} HP ")

class Wheels:
    def __init__(self,size):
        self._size=size

    def show(self):
        print(f"Engine size: {self._size} inches ")

class Car(Engine,Wheels):
    def __init__(self,power,size,model):
        Engine.__init__(self,power)
        Wheels.__init__(self,size)
        self._model=model

    def show(self):
        print(f"Car Model: {self._model}")
        print(f"Engine power: {self._power} HP ")
        print(f"Engine size: {self._size} inches ")

c1 =Car(500,18,'Toyota')
c1.show()
