"""Create a program that takes user input for their name and age.
Use formatted strings (f-strings) to print a message welcoming the user and
stating their age."""

name=input("Enter name: ")
age=int(input("Enter age: "))
print(f"welcome {name} and your age is {age} right")

"""Create a list called numbers that contains integers from 1 to 10.
Check if the number 5 is in the list.
Check if the number 15 is not in the list."""

numbers=[1,2,3,4,5,6,7,8,9,10]
print(5 in numbers)
print(15 not in numbers)
