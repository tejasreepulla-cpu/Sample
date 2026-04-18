# Set Task

"""Task 1: Set Intersection
Write Python code to find and print the intersection of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {4, 5}
"""

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.intersection(set2))

"""Task 2: Set Union
Write Python code to find and print the union of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}
"""

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.union(set2))

"""Task 3: Set Difference
Write Python code to find and print the elements present in set1 but not in set2 :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3}
"""

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.difference(set2))

"""Task 4: Set Symmetric Difference
Write Python code to find and print the symmetric difference of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3, 6, 7, 8}
"""

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.symmetric_difference(set2))

"""Task 5: Set Membership Test
Write Python code to check if the element 3 is present in the set my_set :
my_set = {1, 2, 3, 4, 5}
# Your code here
# Output should be: True
"""

# my_set = {1, 2, 3, 4, 5}
# print(3 in my_set)

"""Exercise 1: Set Intersection
Write a Python script that finds and prints the intersection of two sets."""

# set1=set()
# set2=set()
# len_set1=int(input("Enter length1: "))
# len_set2=int(input("Enter length2: "))
# for i in range(len_set1):
#     element1=input(f"Enter element{i}: ")
#     set1.add(element1)
# for i in range(len_set2):
#     element2=input(f"Enter element{i}: ")
#     set2.add(element2)
# print(set1.intersection(set2))

"""Exercise 2: Set Union
Write a Python script that finds and prints the union of two sets."""

# set1=set()
# set2=set()
# len_set1=int(input("Enter length1: "))
# len_set2=int(input("Enter length2: "))
# for i in range(len_set1):
#     element1=input(f"Enter element{i}: ")
#     set1.add(element1)
# for i in range(len_set2):
#     element2=input(f"Enter element{i}: ")
#     set2.add(element2)
# print(set1.union(set2))

"""Exercise 3: Set Difference
Write a Python script that finds and prints the difference between two sets."""

# set1=set()
# set2=set()
# len_set1=int(input("Enter length1: "))
# len_set2=int(input("Enter length2: "))
# for i in range(len_set1):
#     element1=input(f"Enter element{i}: ")
#     set1.add(element1)
# for i in range(len_set2):
#     element2=input(f"Enter element{i}: ")
#     set2.add(element2)
# print(set1.difference(set2))

"""Exercise 4: Set Symmetric Difference
Write a Python script that finds and prints the symmetric difference between two sets."""

# set1=set()
# set2=set()
# len_set1=int(input("Enter length1: "))
# len_set2=int(input("Enter length2: "))
# for i in range(len_set1):
#     element1=input(f"Enter element{i}: ")
#     set1.add(element1)
# for i in range(len_set2):
#     element2=input(f"Enter element{i}: ")
#     set2.add(element2)
# print(set1.symmetric_difference(set2))

# Tuple task:

"""1. Create a Tuple: Write a program that creates a tuple containing three
elements: your name, your age, and your favorite color. Then print the tuple.
"""

# person_details=()
# list1=list(person_details)
# len_person_details=int(input("Enter length: "))
# for i in range(len_person_details):
#     element=input(f"Enter element{i}: ")
#     list1.append(element)
# print(tuple(list1))

"""2. Access Tuple Elements: Write a program that creates a tuple containing the
days of the week. Then, print the third element of the tuple."""

# days=()
# list1=list(days)
# len_weeks=int(input("Enter length: "))
# for i in range(len_weeks):
#     day=input(f"Enter day{i}: ")
#     list1.append(day)
# days_tuple=tuple(list1)
# print(days_tuple)
# print(days_tuple[2])

"""3. Tuple Concatenation: Write a program that creates two tuples, one
containing odd numbers from 1 to 5 and another containing even numbers
from 2 to 6. Concatenate these two tuples and print the result.
"""

# odd_nums=()
# list1=list(odd_nums)
# even_nums=()
# list2=list(even_nums)
# for i in range(1,7):
#     if i%2!=0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(tuple(list1)+tuple(list2))

"""4. Tuple Unpacking: Write a program that defines a tuple containing the
dimensions of a rectangle (length and width). Then, unpack this tuple into
two variables and calculate the area of the rectangle."""

# length=int(input("Enter length: "))
# width=int(input("Enter width: "))
# dimensions=(length,width)
# length,width=dimensions
# print(length*width)

"""5. Check if an Element Exists: Write a program that checks if a given element
exists in a tuple."""

# tuple_1=()
# list1=list(tuple_1)
# enter_ele=input("Enter ele: ")
# len_tuple_1=int(input("Enter tuple length: "))
# for i in range(len_tuple_1):
#     element=input("Enter element: ")
#     list1.append(element)
# tuple_2=tuple(list1)
# for i in range(len_tuple_1):
#     if enter_ele in tuple_2:
#         print("Element Existed......")
#         break
#     else:
#         print("Element not Existed......")
#         break

# tuple_1=()
# is_exists=False
# list1=list(tuple_1)
# enter_ele=input("Enter ele: ")
# len_tuple_1=int(input("Enter tuple length: "))
# for i in range(len_tuple_1):
#     element=input("Enter element: ")
#     list1.append(element)
# tuple_2=tuple(list1)
# for i in range(len_tuple_1):
#     if enter_ele in tuple_2:
#         is_exists=True
#         break
# print(is_exists)

"""6. Write a Python program to generate a bill for a supermarket purchase. The
program should store the items and their prices in a list of tuples. It should
then iterate over this list to print out each item along with its price. Finally,
calculate and print the total cost of all the items
Sample Input:
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
Sample Output:
Item Price
--------------------
Apple 99.00
Banana 99.00
Milk 49.00
--------------------
Total 247.00"""

# items={}
# total_price=0
# len_items=int(input("Enter length: "))
# for i in range(len_items):
#     item=input("Enter item: ").capitalize()
#     price=float(input("Enter price: "))
#     items[item]=price
#     total_price+=items.get(item)
# print("Item\t\tPrice")
# print("-"*30)
# for item in items:
#     print(f"{item}\t\t{items[item]}")
# print("-"*30)
# print(f"Total\t\t{total_price:.2f}")

# items=[]
# total_price=0
# len_items=int(input("Enter length: "))
# for i in range(len_items):
#     item=input("Enter item: ").capitalize()
#     price=float(input("Enter price: "))
#     items.append((item,price))
#     total_price+=items[i][1]
# print("Item\t\tPrice")
# print("-"*30)
# for i in range(len_items):
#     print(f"{items[i][0]}\t\t{items[i][1]}")
# print("-"*30)
# print(f"Total\t\t{total_price:.2f}")
    