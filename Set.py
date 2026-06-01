#create a set with five numbers
s={1,2,3,4,5}
print(s)

#Add a element to a set
s.add(6)
print(s)

#remove an element using remove() and discard()
s.remove(6)
s.remove(4)
print(s)

#find union, intersection, difference  of two sets
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s2.difference(s1))
print(s1.difference(s2))

#check length of a set
print(len(s))

#convert list to set
lst=[1,2,3,4,1,2]
print(set(lst))

#clear set
s.clear()
print(s)