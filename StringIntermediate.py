#Convert string to lowercase and count vowels
str="PYTHON PROGRAMMING"
print(str.lower().count('a')+str.lower().count('e')+str.lower().count('i')+str.lower().count('o')+str.lower().count('u'))


#Remove spaces and find length
str="python programming"
print(len(str.replace(" ","")))


#Replace spaces with _ and convert to uppercase
str="python programming"
print(str.replace(" ","_").upper())


#Split sentence and print each word
str="python programming".split()
for s in str:
    print(s)


#Count number of words using split()
str="python programming"
print(len(str.split()))


#Find longest word using split()
str="python programming"
print(max(str.split(),key=len))


#Check if substring exists using find()
str="hello world"
if str.find("fi") !=-1:
    print("exists")
else:
    print("not exists")