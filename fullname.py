"'Accept full name and display in reverse order with space between the words.'"
name = input("Enter full name:").split()
for n in name[::-1]:
    print(n,end=' ')
