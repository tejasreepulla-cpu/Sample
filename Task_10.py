#Control Statement:It will control the flow of execution
#1.Conditional Statements:It works based on the outcome of a condition
#Conditional statements are if,if-else,if-elif-else,nested if,nested if-else,shorthand if,shorthand if-else

"""1.if:
    Syntax:
    if condition:
        # indented block of code
        # executed when the condition is true"""
        
age=int(input("Enter age: "))
if(age>=18):
    print("Eligible to vote")
    print("Welcome to voting")
    user=input("Enter name: ")
    print(user)

age=int(input("Enter age: "))
if(age>=18):
    print("Eligible to vote")
    print("Welcome to voting")
    user=input("Enter name: ")
    print(user)
print("you are not eligible")

"""2.else:
Syntax:
if condition:
 # code block to execute if condition is true
else:
 # code block to execute if condition is false
"""
    
age=int(input("Enter age: "))
if(age>=18):
    print("Eligible to vote")
    print("Welcome to voting")
    user=input("Enter name: ")
    print(user)
else:
    print("User is not eligible to vote")

user_name=input("Enter user_name: ")
password=input("Enter password: ")
if(user_name=="swathi" and password=="swathi@123"):
    print("login success")
    print(f"Welcome {user_name}")
print("Invalid credentials")

user_name=input("Enter user_name: ")
password=input("Enter password: ")
if(user_name=="swathi" and password=="swathi@123"):
    print("login success")
    print(f"Welcome {user_name}")
else:
    print("Invalid credentials")

#3.if-elif-else:
"""Syntax:
if condition-1:
 statement 1
elif condition-2:
 stetement 2
elif condition-3:
 stetement 3
 ...
else:
 statement"""
 
marks=int(input("Enter marks: "))
if(marks>=90 and marks<=100):
    print(f"A grade with this marks {marks}")
elif(marks>=80 and marks<=89):
    print(f"B grade with this marks {marks}")   
elif(marks>=70 and marks<=79):
    print(f"C grade with this marks {marks}") 
elif(marks>=60 and marks<=69):
    print(f"D grade with this marks {marks}") 
elif(marks>=50 and marks<=59):
    print(f"E grade with this marks {marks}") 
elif(marks<59 and marks>=0):
    print(f"fail with this marks {marks}") 
else:
    print("Invalid marks....pls enter valid marks")


marks=int(input("Enter marks: "))
if(marks>100 or marks<0):
    print("Invalid marks....pls enter valid marks")
elif(marks>=90):
    print(f"A grade with this marks {marks}")   
elif(marks>=80):
    print(f"B grade with this marks {marks}") 
elif(marks>=70):
    print(f"C grade with this marks {marks}") 
elif(marks>=60):
    print(f"D grade with this marks {marks}") 
elif(marks>=50):
    print(f"E grade with this marks {marks}")
else:
    print(f"fail with this marks {marks}")

"""4.Nested if-else:
Syntax:
if condition1:
 # code block for condition1
 if condition2:
 # code block for condition2
 else:
 # code block for condition2 being false
else:
 # code block for condition1 being false"""
 
name=input("Enter name: ")
password=input("Enter password: ")
if(name=="akhil"):
    if(password=="akhil@123"):
        print("login success")
        print(f"welcome {name}")
    else:
        print("Invalid password...")
else:
    print("Invalid username...")

name=input("Enter name: ")
password=input("Enter password: ")
otp=input("Enter otp: ")
if(name=="akhil"):
    if(password=="akhil@123"):
        if(otp=="12345"):
            print("login success")
            print(f"welcome {name}")
        else:
            print("Invalid otp...")
    else:
        print("Invalid password...")
else:
    print("Invalid username...")

"""5.Short hand if-else:
Syntax:
result = value_if_true if condition else value_if_false"""

num_1=int(input("Enter num_1: "))
result="even number" if(num_1%2==0) else "odd number"
print(result)

num_1=int(input("Enter num_1: "))
print("even number") if(num_1%2==0) else print("odd number")


    