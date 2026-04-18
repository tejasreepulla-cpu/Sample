# Error Handling:
"""Types of Errors:
    1.syntax errors:compiled time errors(easy to identify) but disturbs the flow of execution
    2.runtime errors:errors which disturbs the flow of execution(during the execution) also called Exception
    3.logical errors:user need to identified the errors(very difficult to find)"""
    
# num_1=10
# num_2=5
# res=num_1+num_2
# print(res)

# num_1=10
# num_2=5
# res=num_1-num_2
# print(res)

# print(10+10 #syntax error

# for i in range(10):
# print("hi") #indentation error

# for i in range(10)
#     print("hi") #syntax error

# list_1=[1,2,3
# print(list_1)

# num_1=int(input("enter num_1:"))
# num_2=int(input("enter num_2:"))
# print(num_1+num_2)
# print(num_1-num_2)
# print(num_1*num_2)
# print(num_1/num_2)
# print(num_1+num_2)
# print(num_1-num_2)

# try:code that may raise an exception.If we use try block then it's mandatory to use except block

# num_1=int(input("enter num_1:"))
# num_2=int(input("enter num_2:"))
# print(num_1+num_2)
# print(num_1-num_2)
# print(num_1*num_2)
# try:
#     print(num_1/num_2)
# except:
#     print("error occured")

# else:code to execute if no exception is raised and it's optional

# num_1=int(input("enter num_1:"))
# num_2=int(input("enter num_2:"))
# print(num_1+num_2)
# print(num_1-num_2)
# print(num_1*num_2)
# try:
#     print(num_1/num_2)
# except:
#     print("error occured")
# else:
#     print(num_1+num_2)
#     print(num_1-num_2)

# finally:code to execute regardless of whether an exception was raised or not

# num_1=int(input("enter num_1:"))
# num_2=int(input("enter num_2:"))
# print(num_1+num_2)
# print(num_1-num_2)
# print(num_1*num_2)
# try:
#     print(num_1/num_2)
# except:
#     print("error occured")
# else:
#     print(num_1+num_2)
#     print(num_1-num_2)
# finally:
#     print("No more statements to execute")

# Zero division error:

# num_1=int(input("enter num_1:"))
# num_2=int(input("enter num_2:"))
# try:
#     print(num_1/num_2)
# except ZeroDivisionError as e:
#     print(e)

# Index Error:

# list_1=[1,2,3,4]
# print(list_1[3])
# print(list_1[4])
# print(list_1[0])
# print(list_1[2])

# list_1=[1,2,3,4]
# print(list_1[3])
# try:
#     print(list_1[4])
# except IndexError as e:
#     print(e)
# print(list_1[0])
# print(list_1[2])

# num_1=int(input("Enter num_1:"))
# num_2=int(input("Enter num_2:"))
# print(num_1+num_2)

# Value error:

# try:
#     num_1=int(input("Enter num_1:"))
#     num_2=int(input("Enter num_2:"))
# except ValueError as e:
#     print(e)
# else:
#     print(num_1+num_2)

# Exception Error:

# try:
#     num_1=int(input("Enter num_1:"))
#     num_2=int(input("Enter num_2:"))
# except Exception as e:
#     print(e)
# else:
#     print(num_1+num_2)

# try:
#     num_1=int(input("Enter num_1:"))
#     num_2=int(input("Enter num_2:"))
#     print(num_1/num_2)
#     list_1=[1,2,3,4]
#     print(list_1[10])
# except Exception as e:
#     print(e)

"""ValueError (Raised when an operation or function receives an argument of 
the correct type but an inappropriate value):"""

# try:
#     num=int(input("Enter num: "))
#     num1=int(input("Enter num1: "))
#     print(num+str)
# except ValueError as e:
#     print(f"ValueError: {e}")
# Output:Enter num: 10.2
#        ValueError: invalid literal for int() with base 10: '10.2'

"""TypeError (Raised when an operation or function is applied to an object of an
inappropriate type):"""

# try:
#     num=int(input("Enter num: "))
#     str=input("Enter str: ")
#     print(num+str)
# except TypeError as e:
#     print(f"TypeError: {e}")
# Output:Enter num: 20
#        Enter str: 123
#        TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""FileNotFoundError (Raised when a file or directory is requested but cannot be
found):"""

# try:
#     file=open("C:\\PythonLife\\sample.txt",mode='r')
#     file.close()
# except FileNotFoundError as e:
#     print(f"FileNotFoundError: {e}")
# Output:FileNotFoundError: [Errno 2] No such file or directory: 'C:\\PythonLife\\sample.txt'

"""ZeroDivisionError (Raised when the second operand of a division or module
operation is zero):"""

# try:
#     num=int(input("Enter num: "))
#     num1=int(input("Enter num1: "))
#     result=num/num1
#     print(result)
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError: {e}")
# Output:Enter num: 5
#        Enter num1: 2
#        2.5
# Output1:Enter num: 5
#        Enter num1: 0
#        ZeroDivisionError: division by zero

"""IndexError (Raised when a sequence subscript is out of range):"""

# try:
#     names_list=("raja","rani","sita","gita")
#     print(names_list[2])
#     print(names_list[5])
# except IndexError as e:
#     print(f"IndexError: {e}")
# Output:sita
#        IndexError: tuple index out of range

"""KeyError (Raised when a dictionary key is not found):"""

# try:
#     dict_marks={"raju":92,"ravi":78,"sita":85,"gita":76}
#     print(dict_marks["ramu"])
# except KeyError as e:
#     print(f"KeyError: {e}")
# Output:KeyError: 'ramu'

"""AttributeError (Raised when an attribute reference or assignment fails):"""

# try:
#     class student():
#         def __init__(self,name,marks):
#             self.name=name
#             self.marks=marks
#         def details(self):
#             print(f"student name is {self.names}") 
#     obj=student("Tej",98)  
#     obj.details()    
# except AttributeError as e:
#     print(f"AttributeError: {e}")
# Output:AttributeError: 'student' object has no attribute 'names'

"""OverflowError (Raised when an arithmetic operation exceeds
the limits of the current Python interpreter):"""

# import math
# try:
#     result = math.exp(1000)
#     print(result)
# except OverflowError as e:
#     print(f"OverflowError: {e}")
# Output:OverflowError: math range error

"""IOError (Base class for I/O-related errors):"""

# try:
#     file=open("C:\\PythonLife\\sample.txt",mode='r')
#     read_data=file.read()
#     print(read_data)
#     file.close()
# except IOError as e:
#     print(f"IOError: {e}")
# Output:IOError: [Errno 2] No such file or directory: 'C:\\PythonLife\\sample.txt'

"""RuntimeError (Raised when an error is detected that doesn’t fall in any of the
other categories):"""

# try:
#     num=int(input("Enter num: "))
#     print(name)
# except RuntimeError as e:
#     print(f"RuntimeError: {e}")
# Output:Enter num: 5
#        NameError: name 'name' is not defined

"""Exception (Base class for all exceptions):"""

# try:
#     num=int(input("Enter num: "))
#     list1=[5,6,2,8]
#     print(num+list1)
# except Exception as e:
#     print(f"Exception: {e}")
# Output:Enter num: 5
#        Exception: unsupported operand type(s) for +: 'int' and 'list'






    