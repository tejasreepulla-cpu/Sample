"""Write a Python function square_all(numbers) that takes a list of numbers as input
and returns a new list containing the square of each number in the input list.
Use the map() function with a lambda function to implement this."""

# def square_all(a):
#     return a**2
# list_nums=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list_nums.append(element)
# result=map(square_all,list_nums)
# print(list(result))

# list_nums=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list_nums.append(element)
# result=map(lambda a:a**2,list_nums)
# print(list(result))

"""Write a Python function filter_positive(numbers) that takes a list of numbers as
input and returns a new list containing only the positive numbers from the
input list. Use the filter() function with a lambda function to implement this.
"""

# list_nums=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list_nums.append(element)
# result=filter(lambda a:a>0,list_nums)
# print(list(result))

# def filter_positive(a):
#     if a>0:
#         return a
# list_nums=[]
# length=int(input("Enter length: "))
# for i in range(length):
#     element=int(input("Enter element: "))
#     list_nums.append(element)
# result=filter(filter_positive,list_nums)
# print(list(result))

"""Write a Python function calculate_factorial(n) that calculates the factorial of a
given number n . Use the reduce() function with an appropriate lambda
function to implement this.
"""

# from functools import reduce
# n=int(input("Enter n value: "))
# def calculate_factorial(n):
#     if n<0:
#         return "Invalid entry..."
#     else:
#         return 1 if n==0 else reduce(lambda n,m:n*m,range(1,n+1))
# result=calculate_factorial(n)
# print(result)

"""Write a Python function count_vowels(string) that takes a string as input and
returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce()
function with an appropriate lambda function to implement this.
"""

# from functools import reduce
# n=int(input("Enter n value: "))
# word=input("Enter word: ")
# def count_vowels(word):
#     vowels="aeiouAEIOU"
#     return reduce(lambda count,character:count+1 if character in vowels else count,word,0)
# result=count_vowels(word)
# print(result)



