#Append multiple elements using loop
lst=[2,5,3,4]
for i in range(3):
    n=int(input())
    lst.append(n)
print(lst)


#Sort list in descending order
lst=[5,2,9,1]
lst.sort()
lst.reverse()
print(lst)


#Remove duplicates from list
lst=[1,2,2,3]
s=set(lst)
print(list(s))


#Find second largest number
lst=[2,1,5,8,3]
lst.sort()
print(max(lst[0:len(lst)-1]))

#Copy a list using copy()
lst=[2,1,5,8,3]
cp=lst.copy()
print(cp)


#Merge two lists using +
lst1=[2,1,5,8,3]
lst2=[3,6,4]
print(lst1 + lst2)


#Check if element exists in list
lst=[2,4,7,9]
print(lst.index(9))