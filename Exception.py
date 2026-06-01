#Write a Python program to check whether a number is even or odd using exception handling.
# try:
#     num=int(input("number: "))
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# except ValueError:
#     print("Invalid number")

#Write a program to calculate the average of 3 numbers and handle invalid input
# try:
#     num1=int(input("number: "))
#     num2=int(input("number: "))
#     num3=int(input("number: "))
#     avg=(num1+num2+num3)/3
#     print("average of ",num1," ",num2," ",num3," is ",avg)
# except ValueError:
#     print("Invalid input")

#Write a Python program for simple calculator operations using try and except 
# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     op=input("operation(+,-,*,/): ")
#     if op == '+' :
#         print("Addition: ",num1+num2)
#     elif op == '-' :
#         print("Substraction: ",num1-num2)
#     elif op == '*' :
#         print("Multiplication: ",num1*num2)
#     elif op == '/' :
#         print("Division: ",num1/num2)
#     else:
#         print("invalid operator")
# except ValueError:
#    print("invalid input")
# except ZeroDivisionError:
#    print("division by zero not possible")

#Write a program to take student marks and display grade while handling errors.
# try:
#     mark=float(input("Mark: "))
#     if mark>40:
#         print(" Grade: A")
#     elif mark>30:
#         print(" Grade: B")
#     elif mark>20:
#         print(" Grade: C")
#     elif mark>10:
#         print(" Grade: D")
#     else:
#         print(" Grade: Failed")
# except ValueError:
#     print("Invalid mark")
    
#Write a Python program to handle password validation using custom exceptions
# class InvalidPasswordError(Exception):
#     pass

# try:
#     pwd=input("password: ")
#     if len(pwd) < 8 :
#         raise InvalidPasswordError("password cannot be less than 8 characters")
#     else:
#         print("password accepted")
# except InvalidPasswordError as e:
#     print(e)

#Write a program to read numbers from a file and handle possible exceptions.
# try:
#     file=open("sample.txt","+r")
#     print(file.read())
# except FileNotFoundError:
#     print("file not exits")

#Write a Python program to handle errors while converting string to float.
# try:
#     str=input("enter string: ")
#     num=float(str)
#     print(num)
# except TypeError:
#     print("cannot convert string to float")

#Write a program to remove an item from a list and handle exceptions.
# try:
#     lst=[1,2,3,4]
#     lst.pop(5)
# except IndexError:
#     print("Index does not exist")

#Write a Python program to handle multiple exceptions in a banking application
# try:
#     operation = input("Deposit / Withdraw: ").lower()
#     amt = int(input("Amount: "))
#     balance = 5000

#     if amt <= 0:
#         raise ValueError("Amount must be positive")

#     if operation == "withdraw":
#         if amt > balance:
#             raise Exception("Insufficient Balance")
#         balance -= amt
#         print("Amount Withdrawn")
#         print("Current Balance:", balance)

#     elif operation == "deposit":
#         balance += amt
#         print("Amount Deposited")
#         print("Current Balance:", balance)

#     else:
#         raise NameError("Invalid Operation")

# except ValueError:
#     print("Invalid amount entered")

# except NameError:
#     print("Please enter Deposit or Withdraw only")

# except Exception as e:
#     print(e)

#Write a program to create a login system with exception handling for invalid credentials.
# try:
#     username=input("username:")
#     password=input("password:")
#     if username == "admin" and password == "1234":
#         print("Login Successful")
#     else:
#         raise ValueError("Invalid Credentials")
# except ValueError as e:
#     print(e)



