#Write a Python program to create a file and write data into it.
# file=open("file1.txt","w")
# file.write("hello world")
# file.close()
# file=open("file1.txt","r")
# print(file.read())
# file.close()

#Write a Python program to read a file.
# file=open("example.txt","r")
# print(file.read())
# file.close()

#Write a Python program to append data to a file
# file=open("example.txt","a")
# file.write("\nwelcome to python")
# file.close()
# file=open("example.txt","r")
# print(file.read())
# file.close()

#Write a Python program to read a file line by line.
# file=open("example.txt","r")
# print(file.readline())
# print(file.readline())
# file.close()

#Write a Python program using readlines()
# file=open("example.txt","r")
# print(file.readlines())
# file.close()

#Write a Python program using writelines()
# file=open("example.txt","w")
# lines=['Hello\n','welcome to python\n','file handling\n', 'oops']
# file.writelines(lines)
# file.close()
# file=open("example.txt","r")
# print(file.read())
# file.close()

#Write a Python program demonstrating tell()
# f=open("example.txt","r")
# print(f.read(5))
# print(f.tell())
# f.close()

#Write a Python program demonstrating seek()
# f=open("example.txt","r")
# print(f.read(5))
# print("current cursor position",f.tell())
# print("Moves the cursor to beginning",f.seek(0))
# print("current cursor position",f.tell())
# f.close()

#Write a Python program to create a file using exclusive mode
# file=open("exclusivefile.txt","x")
# file.write("hello world")
# file.close()
# file=open("exclusivefile.txt","r")
# print(file.read())
# file.close()
