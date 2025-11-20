"'Accept a list of single digit numbers as input string. Concatenate the elements of the list as a single number.'"
def concate(l):
    concat=int(''.join(l))
    return concat
    
l= input("Enter a list of number:").split()
print(concate(l))

