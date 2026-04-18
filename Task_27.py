# Function:block of code which only runs when it is called
"""defining a function:
syntax:def function():"""

# def greet():
#     print("welcome to python")
# greet()

# def user_details(): #function defination
#     user=input("Enter user: ")
#     print(user)
# user_details() #function call

# def vote():
#     age=20
#     if age>=18:
#         print("Eligible to vote")
# vote()

# def add(num1,num2):
#     print(num1+num2)
# add(12,3)
# add(15,5)

# def mul(num1,num2):
#     print(num1*num2)
# mul(12,3)

# return statement:
# def mul(num1,num2):
#     return num1*num2
#     name=input("Enter name:")
# print(mul(12,3))

# def mul(num1,num2):
#     return num1*num2
# obj=mul(10,20)
# print(obj)
# print(obj+5)

# arbitary arguments:
# def sample(a):
#     return a
# obj=sample(25)
# print(obj)

# def sample(a,b,c):
#     return a+b+c
# obj=sample(5,6,5)
# print(obj)   
 
# def sample(a):
#     return a
# obj=sample(5,6.5,(1,4,5))
# print(obj) 

# def sample(*a):
#     return a
# obj=sample(5,6.5,(1,4,5))
# print(obj) 

# keyword arguments:
# def sample(**a):
#     return a
# obj=sample(a=1,b=2,c=3)
# print(obj) 

# def details(user,id,dept):
#     print(user,id,dept)
# details("ravi",1234,"frontend")
# details("ram",456,"pythondeveloper")

#default parameters:
# def details(user=None,id=None,dept=None):
#     print(user,id,dept)
# details("ravi",1234,"frontend")
# details("ram",456,"developer")
# details("raju",789,)
# details("ram",)
# details()

# Variables:2 types--->1.local variables:scope inside the function only 2.global variables:scope inside and outside the function
# def details():
#     user="vishnu"
#     id_1=123
#     salary=100000
#     print(user)
#     print(id_1)
#     print(salary)
#     hike=50000
#     salary+=hike
#     print(salary)
# details()
# print(user) #name error

# balance=5000
# def credit(amount):
#     user="kiran"
#     print(user)
#     print(f"credited amount {amount}")
#     print(balance)
# credit(10000)
# print(balance)

# balance=5000
# def credit(amount):
#     user="kiran"
#     print(user)
#     print(f"credited amount {amount}")
#     print(balance)
#     print(f"total balance {balance+amount}")
# credit(10000)
# print(balance)

# balance=5000
# def credit(amount):
#     user="kiran"
#     print(user)
#     print(f"credited amount {amount}")
#     print(balance)
#     balance+=amount
# credit(10000)
# credit(20000)
# print(balance)  #unbound error

# balance=5000
# def credit(amount):
#     global balance
#     user="kiran"
#     print(user)
#     print(f"credited amount {amount}")
#     print(balance)
#     balance+=amount
# credit(10000)
# credit(20000)
# print(balance)

# balance=5000
# def credit(amount):
#     global balance
#     user="kiran"
#     print(user)
#     print(f"credited amount {amount}")
#     print(balance)
#     balance+=amount
# credit(10000)
# print(balance)

#Calculator program
# def add(num1,num2):
#     print(num1+num2)
# def sub(num1,num2):
#     print(num1-num2)
# def mul(num1,num2):
#     print(num1*num2)
# def expo(num1,num2):
#     print(num1**num2)
# add(12,3)
# sub(10,5)
# mul(5,3)
# expo(2,5)

# Modules:collection of functons,every python file is a module
# 3 types:1.userdefined/predefined modules  2.built_in modules 3.third party modules

# 1.user defined models:
# import Task_6
# print(Task_6.list_name_1)

# from Task_6 import *
# print(list_name_1)

# 2.built_in modules
# 1.math
# import math
# print(math.pow(4,4))

# from math import *
# print(pow(4,2))
# print(pi)
# print(sqrt(16))

# 2.random
# from random import *
# print(randint(1,5))
# print(randint(1,5))
# print(choice(["ramu","ravi","raju"]))
# print(choice(["ramu","ravi","raju"]))

# 3.datetime
# from datetime import datetime
# now=datetime.now()
# print(now)


#Functions task:
"""Task 1: Add Function
Write a Python function named add that takes two arguments a and b andreturns their sum."""

# def add(a,b):
#     return a+b
# a=int(input("Enter a value: "))
# b=int(input("Enter b value: "))
# result=add(a,b)
# print(f"Addition of {a} and {b} is {result}")

"""Task 2: Square Function
Write a Python function named square that takes a number x as input and returns its square."""

# def square(x):
#     return x*x
# x=int(input("Enter x value: "))
# result=square(x)
# print(f"Square of {x} is {result}")

"""Task 3: Factorial Function
Write a Python function named factorial that takes a positive integer n as input and returns its factorial."""
# def factorial(n):
#     if n<0:
#         print("Invalid number to perform factorial")
#     else:
#         global fact
#         for i in range(1,n+1):
#             fact*=i
#         print(f"Factorial of {n} is {fact}")
# fact=1
# n=int(input("Enter n value: "))
# factorial(n)

"""Write a Python function named maximum that takes a list of numbers as input and 
returns the maximum value in the list.
"""
# def maximum(list_nums):
#     max=list_nums[0]
#     for ele in list_nums:
#         if ele>max:
#             max=ele
#     return max
         
# list_nums=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=input("Enter element: ")
#     list_nums.append(element)
# result=maximum(list_nums)
# print(result)
    
"""Task 5: Reverse Function
Write a Python function named reverse that takes a string s as input and returns its reverse.
"""
# def reverse(s):
#     return s[ : :-1] 
# s=input("Enter string: ")
# result=reverse(s)
# print(result)

# def reverse(s):
#     global length
#     rs=""
#     for i in range(length):
#         rs+=s[length-i-1]
#     return rs
# length=int(input("Enter length: "))
# s=input("Enter string: ")
# result=reverse(s)
# print(result)

"""Task 6: Check Prime Function
Write a Python function named is_prime that takes a positive integer n as input
and returns True if n is prime, otherwise False .
"""
# def is_prime(n):
#     c=0
#     if n<0:
#         return "Enter positive number only."
#     else:
#         for i in range(1,n+1):
#             if(n%i==0):
#                 c+=1
#         if c==2:
#             return "True"
#         else:
#             return "False"    
# n=int(input("Enter n value: "))
# result=is_prime(n)
# print(result)

"""Task 7: Fibonacci Function
Write a Python function named fibonacci that takes a positive integer n as
input and returns the n th Fibonacci number"""

# def fibonacci(n):
#     if n<=0:
#         return "Enter positive number only."
#     else:
#         a,b=0,1
#         for i in range(2,n):
#             a,b=b,a+b
#         return b  
# n=int(input("Enter n value: "))
# result=fibonacci(n)
# print(result)

"""Task 8: Palindrome Function
Write a Python function named is_palindrome that takes a string s as input and
returns True if s is a palindrome, otherwise False ."""

# def is_palindrome(s):
#     rs=s[ : :-1]
#     if(s==rs):
#         return "True"
#     else:
#         return "False" 
# s=input("Enter s value: ")
# result=is_palindrome(s)
# print(result)

"""Task 9: Sum of Squares Function
Write a Python function named sum_of_squares that takes a list of numbers as
input and returns the sum of the squares of those numbers.
"""
# def sum_of_squares(list_nums):
#     sum=0
#     for item in list_nums:
#         sum+=item
#     return sum       
# list_nums=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list_nums.append(element)
# result=sum_of_squares(list_nums)
# print(result)

"""Task 10: Average Function
Write a Python function named average that takes a list of numbers as input and
returns the average value."""
# def average(list_nums):
#     sum=0
#     for item in list_nums:
#         sum+=item
#     avg=sum/length
#     return avg       
# list_nums=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list_nums.append(element)
# result=average(list_nums)
# print(int(result))