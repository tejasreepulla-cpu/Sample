#Operators
#1.Arthmetic operators--->used to perform mathematical operations
#operand--->variables/values acted upon by an operation to produce a result
#operator--->symbol/keyword used to perform operations on one or more operands
# 1.Addition(+):add 2 operands
num_1=int(input("Enter num_1: "))
num_2=int(input("Enter num_2: "))
print(num_1+num_2)
#2.Subtraction(-):subtracts the right operand from the left operand
print(num_1-num_2)
#3.Multiplication(*):multiplies 2 operands
print(num_1*num_2)
#4.Division(/):divides left operand by the right operand and gives result in float
print(num_1/num_2)
#5.Floor Division(//):divides left operand by the right operand and returns quotient discarding the fractional part.
print(num_1//num_2)
#6.Modules(%):returns remainder of the division
print(num_1%num_2)
#7.Exponentiation(**):raises base to the power of exponent
print(num_1**num_2)

#2.Assignment operator--->used to assign a value to a variable and basic operator is '=' 
# compound operators are +=,-=,*=,/=,//=,%=,**=
num_1=int(input("Enter num_1: "))
num_1+=1
print(num_1)
num_1-=1
print(num_1)
num_1*=1
print(num_1)
num_1/=1
print(num_1)

num_1=int(input("Enter num_1: "))
num_1//=2
print(num_1)

num_1=int(input("Enter num_1: "))
num_1%=2
print(num_1)

num_1=int(input("Enter num_1: "))
num_1**=2
print(num_1)

#3.Comparison Operator--->used to compare values and it returns boolean values
#Comparison Operators are ==,!=,<,>,<=,>=
product_cost=int(input("Enter product_cost: "))
product_cost_1=int(input("Enter product_cost_1: "))
print(product_cost==product_cost_1)
print(product_cost!=product_cost_1)
print(product_cost<=product_cost_1)
print(product_cost>=product_cost_1)
print(product_cost<product_cost_1)
print(product_cost>product_cost_1)

#4.Logical Operators--->used to combine multiple conditions
#Logical operators are and(T-T=T otherwise F),or(F-F=F otherwise T),not(T-F/F-T)
user_name="abhi"
password=123
print(user_name=="abhi" and password==123)
print(user_name=="abhigna" and password==123)
print(user_name=="abhigna" or password==123)
print(user_name=="abhigna" or password==1234)

sample=True
print(not sample)

sample=False
print(not sample)

#5.Identity operators--->used to check if 2 variables are refering to same object
# 1.is:returns true it refers to same object
# 2.is not:returns true it does not refer to same object
list_1=[1,2,3,4]
list_2=[1,2,3,4]
print(id(list_1))
print(id(list_2))
print(list_1 is list_2)

num_1=456
num_2=456
print(id(num_1))
print(id(num_2))
print(num_1 is num_2)

list_1=[1,2,3,4]
list_2=[1,2,3,4]
print(id(list_1))
print(id(list_2))
print(list_1 is not list_2)

#6.Membership Operators--->used to test whether a value is present in a sequence and gives result in boolean
#1.in:returns true if it is present in sequence
#2.not in:returns true if it is not present in sequence
list=["oranges","grapes","mango"]
print("grapes" in list)
print("chikku" in list)
print("grapes" not in list)
print("chikku" not in list)

#Real time example
product_cost=int(input("Enter cost: "))
discount=int(input("Enter discount: "))
res=product_cost*(discount/100)
product_cost-=res
print(product_cost)

#Output Formatting--->used to create dynamic strings by inserting values in placeholder and it is readable,perform calculations
base_value=int(input("Enter base: "))
exp=int(input("Enter exp: "))
print(f"base value {base_value} and exp value {exp} and result is {base_value**exp}")
