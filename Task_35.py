# File Handling:
# read mode:open an existing file for a read operation
# 1.read():returns file content

# file=open("demo.txt",mode='r')
# read_data=file.read()
# print(read_data)
# file.close()

# 2.readline():reads single line

# file=open("demo.txt",mode='r')
# read_data=file.readline()
# print(read_data)
# file.close()

# 3.readlines:read file into a list

# file=open("demo.txt",mode='r')
# read_data=file.readlines()
# print(read_data)
# file.close()

# append mode:open an existing file for append operaton,it won't overriden exiting data

# file=open("sample.txt",mode='a')
# file.close()

# file=open("demo.txt",mode='a')
# write_data=file.write("\nappend operations by using mode a")
# file.close()

"""write mode:open an existing file for a write operaton. If the file already contains 
some data then it will be overriden but if the file is not present then it creates
the file as well"""

# 1.write():writes the specified string to the file

# file=open("demo123.txt",mode='w')
# write_data=file.write("pythonlife")
# file.close()

# 2.writelines():wrtes a list of strings to the file

# voter_data=["vasu\n","raju\n","kiran"]
# file=open("demo123.txt",mode='w')
# write_data=file.writelines(voter_data)
# file.close()

# w+ mode:

# file=open("sample1234.txt",mode='w+')
# write_data=file.write("python is fun")
# read_data=file.read()
# print(read_data)
# file.close()

# r+ mode:

# file=open("demofile.txt",mode='r+')
# write_data=file.write("python is soo fun")
# read_data=file.read()
# print(read_data)
# file.close()

# a+ mode:

# file=open("samplefile.txt",mode='a+')
# write_data=file.write("python is soo fun")
# write_data_1=file.write(" and python is easy to learn")
# read_data=file.read()
# print(read_data)
# file.close()

# tell():returns the current file position

# file=open("sample1234.txt",mode='w+')
# write_data=file.write("data overriden")
# print(file.tell())
# read_data=file.read()
# print(read_data)
# file.close()

# seek():set file pointer position in a file

# file=open("sample1234.txt",mode='w+')
# write_data=file.write("data overriden")
# print(file.tell())
# file.seek(0)
# read_data=file.read()
# print(read_data)
# file.close()

# file deletion:deleting an existng file

# file="sample1234.txt"
# import os
# os.remove(file)

# file rename:renaming an existing file

# file="sample.txt"
# newfile="sample1234.txt"
# import os
# os.rename(file,newfile)

# different directory:

# file=open("C:\Users\hp\OneDrive\Desktop\python.txt",mode='r')
# read_data=file.read()
# print(read_data) #syntax error
# file.close()

# file=open("C:\\Users\\hp\\OneDrive\\Desktop\\python.txt",mode='r')
# read_data=file.read()
# print(read_data)
# file.close()

# file=open("C:\\Users\\hp\\OneDrive\\Desktop\\python123.txt",mode='w')
# file.close()


