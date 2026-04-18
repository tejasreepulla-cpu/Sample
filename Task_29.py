"""Lambda function:
syntax:
    lambda arguments:expression"""

# without using lambda function
# def add(a,b):
#     return a+b
# sum=add(10,5)
# print(sum)

# with using lambda function
# a=int(input("Enter a value: "))
# b=int(input("Enter b value: "))
# add=lambda a,b:a+b
# print(add(a,b))

"""Filter function:
Syntax:
    filter(function,iterable)"""
#Without filter function 
# list_nums=[]
# even_list=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list_nums.append(element)
# for i in list_nums:
#     if i%2==0:
#         even_list.append(i)
# print(even_list)

# def even(a):
#     if a%2==0:
#         return "True"
# result=even(24)
# print(result)

# def even(a):
#     if a%2==0:
#         return "True"
# result=even(24,36,74,94,35)
# print(result) #Type error

# def even(*a):
#     if a%2==0:
#         return "True"
# result=even(24,36,74,94,35)
# print(result)

# list_nums=[24,25,90,24,36,29,13,19,24,20,34,96]
# def even(a):
#     return a%2==0
# result=filter(even,list_nums)
# print(result)
# print(list(result))

# list_nums=[24,25,90,24,36,29,13,19,24,20,34,96]
# result=filter(lambda a:a%2==0,list_nums)
# print(result)
# print(list(result))

"""Map function:
syntax:
    map(function,iter1,iter2,iter3.....)"""
# list1=[5,6,2,8,3,9,2,6,4]
# empty_list=[]
# for i in list1:
#     result=i**2
#     empty_list.append(result)
# print(empty_list)

# def square(a):
#     return a**2
# result=square(4)
# print(result)

# list1=[5,6,2,8,3,9,2,6,4]
# def square(a):
#     return a**2
# result=square(list1)
# print(result) #type error

# list1=[23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# def square(a):
#     return a**2
# result=map(square,list1)
# print(list(result))
# print(result)

# list1=[23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# result=map(lambda a:a**2,list1)
# print(list(result))

# list1=[2,4,5,1,3,6,9,10,8]
# list2=[4,6,7,5,9,3,1,8,10]
# result=map(lambda a,b:a*b,list1,list2)
# print(list(result))

"""Reduce function:
syntax:
    from functools import reduce
    reduce(function,iterable,initializer)"""
# def add(a,b,c,d):
#     return a+b+c+d
# result=add(10,20,30,40)
# print(result)

# from functools import reduce
# list1=[23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# def add(a,b):
#     return a+b
# result=reduce(add,list1)
# print(result)

# from functools import reduce
# list1=[23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# result=reduce(lambda a,b:a+b,list1)
# print(result)

# from functools import reduce
# list1=[4,4,4,4,4]
# result=reduce(lambda a,b:a+b,list1)
# print(result)

# from functools import reduce
# list1=[4,4,4,4,4]
# result=reduce(lambda a,b:a+b,list1,10)
# print(result)

# Generator function:
# def sample():
#     yield 10+5
#     yield 1
#     yield 2
#     yield 3
# obj=sample()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

# def sample():
#     yield 10+5
#     yield 1
#     yield 2
#     yield 3
# obj=sample()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__()) #stopiteration error

