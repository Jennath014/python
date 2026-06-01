#create a dictionary with 3 items and print it
d={"name":"anu",
   "age":21,
   "course":"mca"}
print(d)

#access a value using a key
print(d["name"])

#Add a new value pair
d.update({"college":"MACE"})
'd["college"]="MACE"'
print(d)

#update a value in dictionary
d["age"]=24
print(d)

#Remove a key using pop
d.pop("college")
print(d)

#print all keys
print(d.keys())

#print all values
print(d.values())

#get value using get()
print(d.get("name"))

#copy a dictionary
d2=d.copy()
print(d2)

#clear all items 
d.clear()
print(d)