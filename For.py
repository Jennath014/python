#PYTHON DATA STRUCTURES
#Basic Level
#create a tuple and access elements using indexing
# t=(1,2,3,4)
# print(t[2])

#convert a list into tuple
# lst=[1,2,4,5]
# print(tuple(lst))


#Intermediate Level
#reverse a list without using built-in functions
# lst=[1,2,4,5]
# rev=[]
# for i in lst[::-1]:
#     rev.append(i)
# print(rev)

#merge two lists into one without using +
# l1=[1,2,3]
# l2=[5,6,7]
# l1.extend(l2)
# print(l1)

#create adictionary from 2 lists(key+value)
# l1=["name","age","course"]
# l2=["anu",22,"mca"]
# d=dict()
# for i in range(len(l1)):
#         d[l1[i]]=l2[i]
# print(d)

#remove all even no from list
# lst=[10,2,3,15,16]
# for i in lst[:]:
#     if i%2 ==0:
#         lst.remove(i)
# print(lst)

#flatten a nested list
# nested=[
#       [1,2,3],[4,5,6],[7,8,9]
# ]
# lst=[]
# for i in nested:
#     for j in i:
#         lst.append(j)
# print(lst)

#find missing numbers in a sequence
# lst=[1,3,6,10,12]
# for i in range(lst[0],lst[-1]+1):
#     if i not in lst:
#         print(i)

        
#ADVANCED LEVEL
#rotate a list by k positions
# lst=[1,2,3,4]
# length=len(lst)
# k=2
# while k!=0: 
#     temp=lst[0]
#     for i in range(length):
#         if i != (length-1):
#             lst[i]=lst[i+1]
#     lst[length-1]=temp
#     k-=1
# print(lst)

#find all pairs in a list whose sum is equal to a target
# lst=[3,1,2,4,5]
# target=6
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if  lst[i]+lst[j] == target:
#             print([lst[i],lst[j]])
     
#implement a stack using list
# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print("after pushing values into stack: ",stack)
# stack.pop()
# print("after popping values into stack: ",stack)

#implement a queue using a list
# queue=[]
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print("after inserting values into queue: ",queue)
# queue.pop(0)
# print("after removing values into queue: ",queue)

#find the first non-repeating element in a list
# lst=[1,2,1,2,3,4]
# for i in lst:
#     if lst.count(i)==1:
#         print(i)
#         break
"""length=len(lst)
for i in lst:
    id=lst.index(i)
    if i not in lst[id+1:length]:
        print(i)
        break"""

#group elements by frequency
# lst=[1,3,2,3,1,2,3,4]
# freq={}
# for i in lst:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1   
# group={}
# for key,value in freq.items():
#     if value in group:
#         group[value].append(key)
#     else:
#         group[value]=[key]
# print(group)

#simple hashmap using dictionary
# hashmap={"name":"anu","age":22}
# print(hashmap)

#detect duplicates efficiently
# lst=[1,2,2,2,3]
# print(list(set(lst)))


#FOR LOOP
#Basic
#numbers from 1-10
# for i in range(1,11):
#     print(i,end=" ")

#even no.s btw 1-50
# for i in range(2,50,2):
#     print(i,end=" ")

#sum of n numbers
# n=int(input("num: "))
# s=0
# for i in range(1,n+1):
#     s+=i
# print(s)

#multiplication table of n
# n=int(input("num: "))
# for i in range(1,11):
#     print(i,"*",n,"=",i*n)


#INTERMEDIATE
#count vowels in a string
# str=input("string: ")
# count=0
# for i in str:
#     if i in ['a','e','i','o','u','A','E','I','O','U']:
#         count+=1
# print(count)

#factorial of a n
# n=int(input("num: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#reverse using loop
# str=input("string: ")
# rev=''
# for i in str[::-1]:
#     rev+=i
# print(rev)

#sum of digits of a number
# n=int(input("num: "))
# add=0
# while n>0:
#     rem=n%10
#     add+=rem
#     n=n//10
# print(add)


#Advanced 
#print pyramid pattern
# n=int(input("rows: "))
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("* ",end=" ")
#     print()

#find prime numbers in a range
# for i in range(2,10):
#     for j in range(2,i):
#         if i%j==0:
#             flag=1
#             break
#     else:
#         print(i,end=" ")

#fibonacci series
# a=0
# b=1
# for i in range(10):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

#common elements in 2 loops
# l1=[1,2,3]
# l2=[2,3,4]
# for i in l1:
#     if i in l2:
#         print(i)

#count frequency of elements using loop
# l=[1,2,2,3,3,3]
# freq={}
# for i in l:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)


#WHILE LOOP
#guess the number game
# import random
# num=random.randint(1,100)
# counter=0
# while(1):
#     guess=int(input("guess a number btw 1-100: "))
#     if guess>num:
#         print("Too high")
#         counter+=1
#     elif guess<num:
#         print("Too low")
#         counter+=1
#     else:
#         print("Correct! You guessed it in ",counter," attempts")
#         counter+=1
#         break

#Build a student management system (list + dict + loops)
students=[]
ch=0
while(ch!=6):
    print("Student Menu \n 1. Add Student \n 2. View Students \n 3. Search Student\n 4. Update Student \n 5. Delete Student\n 6. Exit")
    ch=int(input("Choice:"))
    if ch==1:
        id=int(input("Roll no: "))
        name=input("name: ")
        age=int(input("age: "))
        student={"Rollno":id,"Name":name,"age":age}
        students.append(student)

    elif ch==2:
        for student in students:
            print(student)
    
    elif ch==3:
        id=int(input("roll no tp search: "))
        for student in students:
            if id == student["Rollno"]:
                print(student)
        
    elif ch==4:
        id=int(input("Roll no to update: "))
        name=input("new name :")
        for student in students:
            if id == student["Rollno"]:
                student["Name"]=name

    elif ch==5:
        id=int(input("Roll no: "))
        for student in students:
            if id == student["Rollno"]:
                students.remove(student)

    else:
        print("Exiting...!")
        break


