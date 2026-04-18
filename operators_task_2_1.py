"""Write a Python program to calculate the area of a rectangle using the given
formula: area = length * width . Take the values of length and width as inputs from
the user.
"""

length=int(input("Enter length: "))
width=int(input("Enter width: "))
area=length*width
print(area)

#Write a Python program to demonstrate incrementing and decrementing a variable

shirt_price=int(input("Enter shirt_price: "))
shirt_price+=50
print(shirt_price)
pant_price=int(input("Enter pant_price: "))
pant_price-=50
print(pant_price)

"""Write a Python program to convert temperature from Celsius to Fahrenheit. The
formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as
input from the user."""

temperature_celsius=int(input("Enter temperature: "))
fahrenheit=(temperature_celsius*9/5)+32
print(fahrenheit)

"""Write a Python program to calculate the simple interest given the principal
amount, rate, and time (in years)."""

amount=int(input("Enter amount: "))
rate=int(input("Enter rate: "))
time=int(input("Enter time(years): "))
simple_interest=(amount*rate*time)/100
print(simple_interest)

"""Write a Python program to concatenate two strings and display the result. The
strings should be taken as input from the user."""

first_name=input("Enter first_name: ")
second_name=input("Enter second_name: ")
print(first_name+second_name)

"""Write a Python program to convert a distance from kilometers to miles."""
kilometers=int(input("Enter distance in kilometers: "))
miles=kilometers*0.621
print(miles)