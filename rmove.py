"'Write a program to remove all odd indexed characters from a given string.'"
def remove(s):
    r=''
    for i in range(len(s)):
        if i%2 == 0:
            r += s[i]
    return r
        
    
s=input("enter a string:")
print(remove(s))
s='good evening'
print(remove(s))

