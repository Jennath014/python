"'Write a program to search an item in a given list and display the number of occurrences of the given item. '"
def search(n):
    c=0
    for i in l:
        if(i==n):
            c=c+1
    return c
        


l=[1,3,5,7,9,8,5,1,2]
n=int(input("Enter number to search:"))
result=search(n)
if result> 0:
    print("Found element: ",n,"occurence: ", result)
else:
    print("Not found")

