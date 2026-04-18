"""Iterative Statements/Looping Statements:used to execute the block of statements repeatedly
2 types:for loop, while loop"""

"""1.for loop:used to iterate over the sequence
Syntax:
for variable in sequence:
    # code to be executed"""
    
voter_data=["ramu","sita","lakshman","janaki","balaram"]
for i in voter_data:
    print(i)

voter_data=["ramu","sita","lakshman","janaki","balaram"]
for i in voter_data:
    print("Eligible to vote")

fruits=["orange","banana","grape"]
for i in fruits:
    if i=="grape":
        print(f"{i} has received")

"""range():used to generate sequence of numbers and used for iterating over a sequence of numbers in a loop
Syntax:
range(stop)
range(start, stop)
range(start, stop, step)"""

for i in range(10):
    print(i)

for i in range(1,10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(1,11):
    print(f"2 x {i} = {2*i}")

num_1=int(input("Enter num_1: "))
for i in range(1,11):
    print(f"{num_1} x {i} = {num_1*i}")

"""Nested for loop:for loop inside another for loop
Syntax:
for outer_condition:
    # outer loop code
    for inner_condition:
        # inner loop code"""
        
for i in range(3):
    for j in range(3):
        print(i,j)

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print(25*"-")

"""while loop:used to repeatedly execute a block of code as long as a condition is true
Syntax:
while condition:
    # code to be executed"""
    
age=35
while age>=18:
    print("Eligible to vote") #Gives infinite loop

while True:
    user_name=input("Enter user_name: ")
    password=input("Enter password: ")
    if(user_name=="akhil" and password=="akhil@123"):
        print("login successful")
        print(f"welcome {user_name}")
    else:
        print("Invalid credentials")


while True:
    user_name=input("Enter user_name: ")
    password=input("Enter password: ")
    if(user_name=="akhil" and password=="akhil@123"):
        print("login successful")
        print(f"welcome {user_name}")
        break
    else:
        print("Invalid credentials")

count=0
while count<=2:
    print(count)
    count+=1

"""Nested While loop:while loop inside another while loop
Syntax:
while outer_condition:
    # outer loop code
    while inner_condition:
        # inner loop code"""

while True:
    print("Welcome to python")
    while True:
        print("hello everyone") #infinite loop

while True:
    print("Welcome to python")
    break
    while True:
        print("hello everyone")

while True:
    print("Welcome to python")
    while True:
        print("hello everyone") #Infinite loop
        break

while True:
    print("Welcome to python")
    while True:
        print("hello everyone")
        break
    break


        



 
 
 
