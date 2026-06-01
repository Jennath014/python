#Require arguments
#Write a function multiply(a, b)to print multiplication of two numbers.
def multiply(a,b):
    return a*b
a=5
b=4
print(multiply(a,b))

#Create a function student(name, mark) and display student details.
def student(name, mark):
    print("Student details:\n name : "+name+"\n mark : ",mark)
student("anu",45)

# Write a function to find the area of a rectangle using length and breadth.
def area(length,breadth):
    return length*breadth
print("area of rectangle with side 4 and 5: ",area(4,5))

#Create a function evenodd(num) to check whether a number is even or odd.
def evenodd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
evenodd(5)

#Write a function greet(name) that prints:"Welcome <name>"
def greet(name):
    print("Welcome "+name)
greet("john")


#Keyword Arguments
#Create a function employee(name, salary) and call it using keyword arguments.
def employee(name, salary):
    print("employee details:\n name : "+name+"\n salary : ",salary)
employee(name="john",salary=25000)    

#Write a function movie(title, year) and pass arguments in different order.
def movie(title, year):
    print("movie title: "+title+"\n year: ",year )
movie(year=2000,title="anaconda")

#Create a function product(name, price) using keyword arguments
def product(name, price):
    print("product details:\n name : "+name+"\n price : ",price)
product(name="laptop",price=85000)

#Write a function person(name, city) and display details.
def person(name, city):
    print("person details:\n name : "+name+"\n city : "+city)
person(name="john",city="london")

#Create a function book(title, author) and call it using keywords.
def book(title, author):
    print("book details:\n title : "+title+"\n author : "+author)
book(title="dracula",author="bramstoker")


#Default Arguments
#Write a function country(name="India")
def country(name="India"):
    print(name)
country()
country("london")

#Create a function power(a, b=2) to find square by default.
def power(a, b=2):
    return a**b
print(power(2))
print(power(2,4))

#Write a function welcome(name="Guest")
def welcome(name="Guest"):
    print("Welcome "+name)
welcome()
welcome("john")

#Create a function salary(amount=10000)
def salary(amount=10000):
    print(amount)
salary()
salary(20000)

#Write a function 
def student(course="MCA"):
    print(course)
student("bca")
student()


#Variable-Length Arguments (args)
#Write a function to find sum of any number of values.
def summation(*args):
    return sum(args)
    total=0
    for i in args:
        total+=i
    print(total)
print(summation(1,2,3,4,5))

#Create a function to print all given names.
def names(*args):
    for i in args:
        print(i)
names("john","anu","riya")

#Write a function to find largest number using args 
def largest(*args):
    # print(max(args))
    large=args[0]
    for i in args:
        if i > large:
            large=i
    print(large)
largest(1,2,3,4,5)

#Create a function to calculate average of numbers.
def avg(*args):
    length=len(args)
    total=0
    for i in args:
        total+=i
    print(total/length)
avg(1,2,3,4,5)

#Write a function to count total arguments passed.
def count(*args):
    return len(args)
print(count(1,2,3,4))


#Variable-Length Keyword Arguments (*kwargs )
#Write a function to display student details using *kwargs
def student(**kwargs):
    print(kwargs) 
student(name="jon",age=22,course="mca")

#Create a function to print employee information.
def employee(**kwargs):
    print(kwargs) 
employee(name="jon",age=22,dept="it")

#Write a function to display product details.
def product(**kwargs):
    print(kwargs) 
product(name="icecream",price=40)

#Create a function to store customer information dynamically.
def customer(**kwargs):
    print(kwargs)
name=input("Customer name: ")
phoneno=int(input("phone no:"))
product=input("product: ")
customer(customername=name,phoneno=phoneno,product=product)

#Write a function that accepts any number of keyword arguments and prints them.
def keyargs(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)
keyargs(name='joy',age=22,course='mca',dept='it',college='ma')


#Mini Practical Programs
#Create a calculator using functions.
#Write a menu-driven program using functions.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    print("Result =", divide(a, b))
else:
    print("Invalid choice")

#Create a student marklist using functions and arguments.
def marklist(name,m1,m2,m3):
    total=m1+m2+m3
    grade=''
    avg=total/3
    if avg>40:
        grade='A'
    elif avg>30:
        grade='B'
    elif avg>20:
        grade='C'
    elif avg>10:
        grade='D'
    else:
        grade='fail'
    print("Marklist:\n Name:"+name)
    print(" Total:",total)
    print(" Average:",avg)
    print(" Grade:"+grade)

marklist('john',45,23,37)

#Build a simple billing system using function arguments.
def bill(item,qnty,price):
    total = qnty * price
    print("Bill:\nitem:"+item+" qnty:",qnty," price:",price)
    print("total bill",total)
bill('chocolates',5,35)

#Create a login function using username and password arguments.
def login(username, password):
    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Invalid Credentials")

name=input("username:")
pwd=input("password:")
login(name,pwd)