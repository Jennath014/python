l='banana,apple,fig,cherry'
w=[w.strip() for w in l.split(",")]
w.sort(key = len)
print(w)
