d={1:'a',
   2:'b',
   3:'c'
   }
k=int(input("Key to check:"))
print(k in d)

"'merge two dictionaries'"
d1={1:10,2:20,3:30,4:40}
d2={5:50,6:60,7:70}
d1.update(d2)
print(d1)

"'dictionary sort'"
d={2:20,1:2,6:12,3:1}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),reverse=True)))

"'inverted dictionary'"
i={value:key for key,value in d.items()}
print(i)
