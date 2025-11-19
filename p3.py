c1=['red','green','blue']
c2=['pink','white','green']

print([c for c in c1 if c not in c2])
diff = set(c1).difference(set(c2))
print(diff)

l=[2,3,4,2,3,1,9]
print(list(set(l)))

if len(l)==0:
    print("list empty")
else:
    print("list not empty")
