n = int(input("Rows: "))

for i in range(1, n + 1):
    
    print(" " * (n - i), end="")

    
    for j in range(1, i + 1):
        print("*", end="")

        if j < i:
            print("  ", end="")
    print() 

