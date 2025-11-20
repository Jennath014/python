"'Write a program to print all even numbers from a given list in the given order until you reach number 237 or end of the list. '"
def even(i):
        if i%2 == 0:
            return i

l=[12,323,4,17,2,23,234,123,42,122,237,46]
for i in l:
    if i == 237:
        break
    if even(i):
        print(i)
m=input("enter a list:")
m=list(map(int,m.split()))
for i in m:
    if i == 237:
        break
    if even(i):
        print(i)
