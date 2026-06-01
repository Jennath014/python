#Use append() to add "orange" to list
lst=['apple','pineapple','grape']
lst.append('orange')
print(lst)


#Use insert() to insert "grapes" at index 1
lst=['apple','pineapple','orange']
lst.insert(1,'grapes')
print(lst)


#Use remove() to remove "banana"
lst=['apple','pineapple','grape','banana']
lst.remove('banana')
print(lst)


#Use pop() to remove last element
lst=['apple','pineapple','grape','banana']
print(lst)
lst.pop()
print(lst)


#Use len() to find length of list
lst=['apple','pineapple','grape','banana']
print(len(lst))


#Use count() to count occurrences of 2 in [1,2,2,3]
lst=[1,2,2,3]
print(lst.count(2))


#Use sort() to sort [5,2,9,1]
lst=[5,2,9,1]
lst.sort()
print(lst)


#Use reverse() to reverse list
lst=['apple','orange','banana']
print(lst[::-1])