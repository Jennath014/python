#Remove duplicate characters using functions
def remove_duplicate(str):
    result=""
    for i in str:
        if i not in result:
            result+=i
    return result

str="hello world"
print(remove_duplicate(str))


#Reverse string using slicing

str="hello world"
print(str[::-1])


#Check palindrome using functions

str="mom"
rev = str[::-1]
if str == rev:
    print("palindrome")
else:
    print("not palindrome")


#Convert "hello world" -> "hElLo WoRlD" (alternate case)
str1="hello world"
s=str1.lower()
d=list(s)
for i in range(0,len(s),2):
    d[i]=s[i].upper()
print("".join(d))


#Extract only alphabets from "abc123@#"
str="abc123@#"
res=""
for s in str:
    if s.isalpha():
        res+=s
print(res)

