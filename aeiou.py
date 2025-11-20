s1=input("enter the string :")
result=s1[::2]
print(result)
vowels="aeiou"
count=sum(1 for char in s1 if char in vowels)
print(count)
