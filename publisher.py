"'create a class Publisher(name).'"
"'Derive a class BOOk (title,Autor) from publisher.'"
"'Derive a class Python (price,no of pages) from Book.'"
"'write a program that displays information about a python  book.'"
"'Use base class constructor invocation and method overriding'"


class Publisher:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"Publisher Name: {self.name}")

class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author

    def show(self):
        super().show()
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        
class Price(Book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price=price
        self.pages=pages

    def show(self):
        super().show()
        print(f"Price: ₹{self.price}")
        print(f"No. of Pages: {self.pages}")

p1=Price('B&B','Oliver twist','Charles Dickens',200,180)
p1.show()

        

