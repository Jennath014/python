class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book("Python Guide", "Guido")
b.publisher = "O'Reilly"     # runtime attribute

if hasattr(b, "publisher"):
    print(f"{b.title} written by {b.author} is published by {b.publisher}")
else:
    print("Unknown Publisher")
