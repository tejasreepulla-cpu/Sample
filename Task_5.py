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

#Declare two variables, one storing an integer and the other a string. Print their values.
num_1=int(input("Enter number: "))
word=input("Enter string: ")
print(num_1)
print(word)

#Write a program that prints a pattern using multiple print statements.
print("Hello")
print("World")
print("I am python user")
print("Python is very easy to learn")

# #Create a Python script for a simple task and add comments to explain each step
line_1=input("Enter line_1: ") #User is reading string input and storing it in line_1 variable
line_2=input("Enter line_2: ") #User is reading string input and storing it in line_2 variable
print(line_1+line_2) #doing string concatenation by using + operator

#Create variables of different data types(int,float,str) and print their values.
num_1=int(input("Enter num_1 value: "))
num_2=float(input("Enter num_2 value: "))
word=input("Enter word value: ")
print(num_1)
print(num_2)
print(word)

# Determine the data type of a variable.
# Expected Output:
# The data type of variable discount is <class 'int'>.

num_1=int(input("Enter num_1 value: "))
print("The data type of variable discount is "+str(type(num_1)))

#Display the memory addresses
# The memory addresses of x and y
employee_id = 10
person_age = 10
print("The memory addresses of employee_id and person_age",id(employee_id),id(person_age))

#Create a program that takes user age = “35”, converts it to an integer,and then prints the result type.
age="35"
num=int(age)
print(type(num))

#Concatenate two strings and print the result.
word_1=input("Enter word_1 value: ")
word_2=input("Enter word_2 value: ")
print(word_1+word_2)




