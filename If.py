#BASIC 
#check if a number is +ve or -ve
n=int(input("number:"))
if n>0:
    print(n," is +ve")
else:
    print(n," is -ve")

#check if a number is even or odd
n=int(input("number:"))
if n%2==0:
    print("Even")
else:
    print("Odd")

#check if a person is elegible to vote age>=18
age=int(input("age:"))
if age>=18:
    print("eligible")
else:
    print("not eligible")

#check if a number is greater than 100
num= int(input("number:"))
if num>100:
    print("greater than 100")
else:
    print("less than 100")

#check if two numbers are equal
a=int(input("number1:"))
b=int(input("number2:"))
if a==b:
    print("numbers are equal")
else:
    print("numbers are not equal")


#INTERMEDIATE 
#find greatest of 2 numbers
a=int(input("number1:"))
b=int(input("number2:"))
if a>b:
    print(a," is greater than ",b)
elif b>a:
    print(b," is greater than ",a)
else:
    print("both are equal")

#largest of 3 numbers
a=int(input("number1:"))
b=int(input("number2:"))
c=int(input("number3:"))
largest=a
if b>largest:
    largest=b
if c>largest:
    largest=c
print(largest)

#check if a number is divisible by 5
a=int(input("number:"))
if a%5==0:
    print(a," is divisible by 5 ")
else:
    print(a,"not divisible by 5")

#check if a number is divisble by both 3 and 5:
a=int(input("number:"))
if a%3==0 and a%5==0:
    print("number is divisble by both 3 and 5")
else:
    print("number is not divisble by both 3 and 5")

#check if a year is leap year
year= int(input("year:"))
if (year%100 !=0 and year%4==0) or  year%400==0:
        print("leap year")
else:
    print("not leap year")


#STRING BASED
#check if a string is empty
str=input("enter string")
if str == "":
    print("string empty")
else:
    print(str)

#checks if a string starts with a vowel
str=input("enter string:")
if str.startswith(('a','e','i','o','u','A','E','I','O','U')):
    print("starts with vowel")
else:
    print("doesn't starts with vowels")

#check if 2 strings are equal
str1=input("enter string: ")
str2=input("enter string: ")
if str1.casefold() == str2.casefold():
    print("two strings are equal")
else:
    print("not equal")

#check if a word is in uppercase
str=input("enter string: ")
if str.isupper():
    print("word is in uppercase")
else:
    print("word is not in uppercase")

#check if a character is alphabet or not
c=input("Enter character: ")
if c.isalpha():
    print("character")
else:
    print("not")

#REAL LIFE BASED 
#check login (username and password)
user=input("enter username: ")
pwd=input("enter password: ")
print("To Login")
u1=input("enter username: ")
pwd1=input("enter password: ")
if u1 == user and pwd1 == pwd:
    print("Login success")
else:
    print("Incorrect username or password")

#check pass/fail , marks >=50
mark=int(input("Enter mark: "))
if mark>=50:
    print("Passed")
else:
    print("Failed")

#Grade system A, B, C, Fail
mark=int(input("Enter mark out of 50: "))
if mark>=40:
    print("A grade")
elif mark>=30:
    print("B grade")
elif mark>=20:
    print("C grade")
else:
    print("Fail")

#check if a number is within range[1-100]
num=int(input("number:"))
if num>=0 and num<=100:
    print("number is between 1-100")
else:
    print("not in range")

#simple calculator based on +,-,/,*
num1=int(input("number:"))
num2=int(input("number:"))
op=input("operation(+,-,*,/): ")
if op == '+' :
    print("Addition: ",num1+num2)
elif op == '-' :
    print("Substraction: ",num1-num2)
elif op == '*' :
    print("Multiplication: ",num1*num2)
elif op == '/' :
    print("Division: ",num1/num2)
else:
    print("invalid operator")


#NESTED IF
#find largest of 3 numbers
a=int(input("number1:"))
b=int(input("number2:"))
c=int(input("number3:"))
if a>b :
    if  a>c:
        largest=a
    else:
        largest=c
else:
    if b>c:
        largest=b
    else:
        largest=c
print(largest)

#check triangle type(equilateral,isosceles,scalene)
a=int(input("number1:"))
b=int(input("number2:"))
c=int(input("number3:"))
if a==b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")

#check if a number is +ve,-ve,0
num=int(input("number:"))
if num!=0:
    if num>0:
        print("+ve")
    else:
        print("-ve")
else:
    print("zero")

#ATM withdrawal condition , balance check
amt=int(input("Enter amount: "))
balance=1000
if balance>0:
    if amt>balance:
        print("Insufficient balance")
    else:
        balance-=amt
        print("amt withdrawed")
else:
    print("Zero balance")
    
#check discount elgibility based on amount
amt=int(input("Enter amount: "))
if amt>=500:
    if amt>=2000:
        print("25% of discount")
    elif amt>=1000:
        print("10% discount")
    else:
        print("5% discount")
else:
    print("no discount")


#CHALLENGE QUESTIONS
#check palindrome (number/ string)
num=int(input("number:"))
temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if temp==rev:
    print("Palindrome")
else:
    print("not palindrome")

#check armstrong number
num=int(input("number:"))
temp=num
arm=0
while num>0:
    rem=num%10
    arm=arm+rem*rem*rem
    num=num//10
if temp==arm:
    print("Armstrong")
else:
    print("not Armstrong")

#check if a character is vowel or consonant
ch=input("character: ")
if ch in ['a','e','i','o','u']:
    print("vowels")
else:
    print("Consonant")

#menu-based program using if-elif
num1=int(input("number:"))
num2=int(input("number:"))
print("Menu \n 1.Add \n 2. Sub \n 3. Mul \n 4. Div \n")
ch=int(input("choice: "))
if ch == 1 :
    print("Addition: ",num1+num2)
elif ch == 2 :
    print("Substraction: ",num1-num2)
elif ch == 3 :
    print("Multiplication: ",num1*num2)
elif ch == 4 :
    print("Division: ",num1/num2)
else:
    print("invalid operator")

#check if a number lies between two numbers
num = int(input("Enter number: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < num < b:
    print("Number lies between")
else:
    print("Number does not lie between")