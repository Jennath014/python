class Flower:
    def __init__(self, name):
        self.name = name

f = Flower("Rose")
f.petalColor = "Red"

if hasattr(f, "petalColor"):
    print(f"{f.petalColor} {f.name}")
else:
    print("Unknown Flower")
