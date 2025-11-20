n=int(input("enter limit:"))
a,b=0,1
l=[0,1]
for i in range(1,n-1):
    a,b=b,a+b
    l.append(b)
print("fibonacci sequence",l)

m=int(input("position:"))
[print("element  at position",m,":",l[m-1]) if m<=len(l) else print("not found")]





