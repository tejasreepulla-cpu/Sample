"""1.Vowel Checker:
Write a Python program that takes a character as input and checks whether
it is a vowel or not. Use the
if-else statement."""

character=input("Enter character: ")
vowels="aeiouAEIOU"
if character in vowels:
    print(f"{character} is a vowel")
else:
    print(f"{character} is not a vowel")
    
character=input("Enter character: ")
vowels_list=['a','e','i','o','u','A','E','I','O','U']
if character in vowels_list:
    print(f"{character} is a vowel")
else:
    print(f"{character} is not a vowel")   
    
character=input("Enter character: ")
vowels_list=('a','e','i','o','u','A','E','I','O','U')
if character in vowels_list:
    print(f"{character} is a vowel")
else:
    print(f"{character} is not a vowel")  

character=input("Enter character: ")
if character == 'a'or character =='e'or character =='i'or character =='o'or character =='u'or character == 'A'or character =='E'or character =='I'or character =='O'or character =='U':
    print(f"{character} is a vowel")
else:
    print(f"{character} is not a vowel") 
    
character=input("Enter character: ")
if character == 'a'or 'e' or 'i' or 'o' or 'u' or 'A'or 'E' or 'I' or 'O' or 'U':
    print(f"{character} is a vowel")
else:
    print(f"{character} is not a vowel") 

"""2.Age Group Classification
Write a program that takes an age as input and classifies the person into
one of the following age groups:
Child: 0-12 years
Teenager: 13-17 years
Adult: 18-64 years
Senior: 65 years and older"""

age=int(input("Enter age: "))
if(age<0):
    print("Invalid age.. pls enter valid age")   
elif(age>=0 and age<=12):
    print("Child")
elif(age>=13 and age<=17):
    print("Teenager")
elif(age>=18 and age<=64):
    print("Adult")
else:
    print("Older")

"""3. Number Classifier:
Write a program that takes an integer as input and classifies it as positive,
negative, or zero. Use the
if-elif-else statement."""

num_1=int(input("Enter num_1: "))
if(num_1>0):
    print("Positive Number")
elif(num_1<0):
    print("Negative Number")
else:
    print("Zero")

"""4. Leap Year Checker:
Create a program that checks whether a given year is a leap year or not. A
leap year is divisible by 4, but not by 100 unless it is divisible by 400."""

year=int(input("Enter year: "))
if year%4==0:
    if year%100!=0 or year%400==0:
        print(f"{year} is a Leap year")
else:
    print(f"{year} is not a leap year")

year=int(input("Enter year: "))
if (year%4==0) and (year%100!=0 or year%400==0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a leap year")

"""5. Calculator:
Build a simple calculator program that takes two numbers and an operator
(+, -, *, /) as input and performs the corresponding operation.
"""

num_1=int(input("Enter num_1: "))
num_2=int(input("Enter num_2: "))
operator=input("Enter operator: ")
if operator=='+':
    print(f"Addition of {num_1} and {num_2} is {num_1+num_2}")
elif operator=='-':
    print(f"Subtraction of {num_1} and {num_2} is {num_1-num_2}")
elif operator=='*':
    print(f"Multiplication of {num_1} and {num_2} is {num_1*num_2}")
elif operator=='/':
    print(f"Division of {num_1} and {num_2} is {num_1/num_2}")
else:
    print("Invalid operator...pls enter valid operator")

"""6. Short Hand If:
Rewrite the following code using the short-hand
if statement:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"""

num_1=int(input("Enter num_1: "))
result="Even" if num_1%2==0 else "Odd"
print(result)

num_1=int(input("Enter num_1: "))
print("Even") if num_1%2==0 else print("Odd")

"""7. Discount Calculator:
Create a program that calculates the final price after applying a discount.
The program should take the original price and the discount percentage as
input."""

product_cost=int(input("Enter product_cost: "))
discount_percent=int(input("Enter discount_percent: "))
result=product_cost*(discount_percent/100)
product_cost-=result
print(product_cost)

"""8. BMI Calculator:
Write a program that calculates the Body Mass Index (BMI) using the
formula: BMI = weight (kg) / (height (m))^2. The program should take
weight and height as input."""

weight=int(input("Enter weight(kg): "))
height=float(input("Enter height(m): "))
bmi=weight/(height**2)
print(bmi)


