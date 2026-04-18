"""Reverse List:
Write Python code to reverse the order of elements in the given list my_list .
Print the reversed list."""

# my_list = [10, 20, 30, 40, 50, 11]
# print(my_list[ : :-1])

# my_list = [10, 20, 30, 40, 50, 11]
# my_list.reverse()
# print(my_list)

"""Given two lists list1 and list2 , find and print the common elements between
them."""

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_list=[]
# for i in list1:
#     if i in list2:
#         common_list.append(i)
# print(common_list)

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_list=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             common_list.append(i)
# print(common_list)

"""Unique Elements:
Create a new list unique_list containing only the unique elements from the
given list original_list . Print the unique list.
"""

# original_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements=[]
# for i in original_list:
#     if i not in unique_elements:
#         unique_elements.append(i)
# print(unique_elements)

# original_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements=[original_list[0]]
# for i in range(1,len(original_list)):
#     if(original_list[i]!=original_list[i-1]):
#         unique_elements.append(original_list[i])
# print(unique_elements)

"""Remove Duplicates:
Remove duplicate elements from the given list duplicated_list and print the list
without duplicates while preserving the order.
"""

# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements=[]
# for i in duplicated_list:
#     if i not in unique_elements:
#         unique_elements.append(i)
# print(unique_elements)

# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements=[duplicated_list[0]]
# for i in range(1,len(duplicated_list)):
#     if(duplicated_list[i]!=duplicated_list[i-1]):
#         unique_elements.append(duplicated_list[i])
# print(unique_elements)

"""Exercise 1: List Concatenation
Write a Python script that concatenates two lists and prints the result.
"""

# list1=[]
# list2=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list1.append(element)
# for i in range(length):
#     element1=int(input("Enter element1: "))
#     list2.append(element1)
# print(list1+list2)
    
    
"""Exercise 2: List Repetition
Write a Python script that repeats a list three times and prints the result."""

# list1=[]
# length=int(input("Enter length: "))
# num_1=int(input("Enter num_1: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list1.append(element)
# print(list1*num_1)

"""Exercise 3: List Removal
Write a Python script that removes the elements at even indices from a list."""
    
# list1=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list1.append(element)
# result=[list1[i] for i in range(length) if i%2!=0]
# print(result)

# list1=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list1.append(element)
# list2=[]
# for i in range(length):
#     if i%2!=0:
#         list2.append(list1[i])
# print(list2)

"""Exercise 4: List Insertion
Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of
a list"""

# list1=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list1.append(element)
# list1.insert(0,12)
# list1.insert(0,11)
# list1.insert(0,10)
# print(list1)

# list1=[]
# list2=[10,11,12]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list1.append(element)
# list1=list2+list1
# print(list1)

# List comprehensions:
# 1. Square Numbers: Create a list of squares of numbers from 1 to 10.

# length=int(input("enter length: "))
# result=[i**2 for i in range(1,length+1)]
# print(result)

# length=int(input("enter length: "))
# print([i**2 for i in range(1,length+1)])

# 2. Even Numbers: Generate a list of even numbers from 1 to 20.

# length=int(input("enter length: "))
# result=[i for i in range(1,length+1) if i%2==0]
# print(result)

# length=int(input("enter length: "))
# print([i for i in range(1,length+1) if i%2==0])

# 3. Words Lengths: Given a list of words, create a list containing the lengths of each word.
# words = ["apple", "banana", "cherry", "date"]

# list1=[]
# length=int(input("enter length: "))
# for i in range(length):
#     element=input("enter element: ")
#     list1.append(element)
# list2=[]
# for i in range(length):
#     list2.append(len(list1[i]))
# print(list2)

# list1=[]
# length=int(input("enter length: "))
# for i in range(length):
#     element=input("enter element: ")
#     list1.append(element)
# count_words=[len(list1[i]) for i in range(length)]
# print(count_words)

# list1=[]
# length=int(input("enter length: "))
# for i in range(length):
#     element=input("enter element: ")
#     list1.append(element)
# print([len(list1[i]) for i in range(length)])
    
    





 