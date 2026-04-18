#Write a Python program that prints your name

print("Tejasree")

#Create a Python script with both single-line and multi-line comments explaining the purpose of the script.

#Below code is addition of 3 numbers using input function
num_1=int(input("Enter num_1 value:"))
num_2=int(input("Enter num_2 value:"))
num_3=int(input("Enter num_3 value:"))
"""user is reading 3 input values 
   i.e num_1,num_2,num_3
   and then adding 3 numbers and storing the result in result variable"""
result=num_1+num_2+num_3
print(result)

#Define a list containing three different data types.
list=[123,23.5,"python"]
print(list)

#Define a set containing employee id’s.
emp_id={101,102,103,104}
print(emp_id)

#Concatenate two strings and print the result
str_1=input("Enter str_1: ")
str_2=input("Enter str_2: ")
print(str_1+str_2)

#Repeat a string three times and display the output.
str_1=input("Enter str_1: ")
print(str_1*3)

str_1=input("Enter str_1: ")
value=int(input("Enter value: "))
print(str_1*value)

#Create a variable with a name that is a Python keyword. What happens? observation..
if="abc"
print(if)  #getting syntax error b/c variable names should not match with python keywords

#Declare two variables, one storing an integer and the other a string.Print their values.
num=int(input("Enter num: "))
str=input("Enter str: ")
print(num)
print(str)

#Convert a float to an integer and print the result.
num_1=float(input("Enter num_1: "))
num_2=int(num_1)
print(num_2)

#Convert an integer to a string and display the output.
num_1=int(input("Enter num_1: "))
str=str(num_1)
print(str)
print(type(str))

#Take the user's age as input and print a message using that input.
age=int(input("Enter age: "))
print("Raju's age is"+" "+str(age))
print("Raju's age is %d"%(age))
print("Raju's age is",age)
print("Raju's age is {0}".format(age))

#Write a program that prints a pattern using multiple print statements.
print("Hi")
print("How are you?")
print("I am fine")
print("What about you?")

#Create a Python script for a simple task and add comments toexplain each step.
line_1=input("Enter line_1: ") #User is reading string input and storing it in line_1 variable
line_2=input("Enter line_2: ") #User is reading string input and storing it in line_2 variable
print(line_1+line_2) #doing string concatenation by using + operator

#Implement a program that uses a dictionary to store information about a book (title, author, publication year).
dict={"title":"python","author":"Guido van Rossum","publication_year":1991}
print(dict)

#Write a python program that takes a string as input ( 35 ) and return float value.
str=input("Enter str :")
num=int(str)
num_1=float(num)
print(num_1)

#Write a program to take two names as input and print them together.
name_1=input("Enter name_1: ")
name_2=input("Enter name_2: ")
print(name_1+name_2)

#Create a program that takes user input for their age, converts it to an integer, adds 5, and then prints the result.
str=input("Enter str: ")
age=int(str)
age+=5
print(age)

#Build a calculator program that takes two numbers as input and performs the arithmetic operation.
num_1=int(input("Enter num_1: "))
num_2=int(input("Enter num_2: "))
print(num_1+num_2)
print(num_1-num_2)
print(num_1*num_2)
print(num_1/num_2)
print(num_1%num_2)
print(num_1//num_2)
print(num_1**num_2)
