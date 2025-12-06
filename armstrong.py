for n in range(100, 501):
    s = sum(int(d)**3 for d in str(n))
    if s == n:
        print(n)
