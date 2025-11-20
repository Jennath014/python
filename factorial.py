n=int(input("Enter a number:"))
f=1
if(n<0):
    print("Negative numbers have no factorial")
else:
     for i in range(1,n+1):
         f*=i
     print("factorial of", n,"is",f)


            
