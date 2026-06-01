#Sort list without using sort()
lst=[2,9,1,6,7]
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]<lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)

#Find frequency of each element (use list + dictionary)
lst=[1,2,2,4,1]
d=dict()
for i in lst:
    if i not in d:
        value=1
    else:  
        value+=1
    d[i]=value
print(d)

#Remove all occurrences of a value
lst=[1,2,2,4,7]
value=2
while value in lst:
    lst.remove(value)
print(lst)


#Rotate list [1,2,3,4] → [2,3,4,1]
lst=[1,2,3,4]
temp=lst[0]
length=len(lst)
for i in range(length):
    if i != (length-1):
        lst[i]=lst[i+1]
lst[length-1]=temp
print(lst)

#Split list into even and odd numbers
lst=[1,2,3,4]
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even,odd)

