"""data types--->Types of data types are of 2 types
They are 1.Mutable 2.Immutable
Mutable datatype is defined as once we create an object we can do modifications on that object and it refers to the same object 
Mutable datatypes are Lists,dictionarys,sets
Immutable datatype is defined as once we create an object we can't do modifications on that object if we try to do modifications using built-in datatypes it will return the copy of that object
immutable datatypes are Numbers,tuple,strings
"""
#1.List--->ordered sequence of elements and allows different datatypes,mutable,enclosed in [] and separated with commas
# list=[10,30.2,"python"]
# print(list)
# print(id(list))
# print(type(list))

# list.append('welcome') #append function is used to add the elements at the end of the list
# print(list)
# print(id(list))

#2.Tuple--->ordered sequence of elements and allows different datatypes,immutable,enclosed in () and separated with commas
# tuple=(10,30.2,"python")
# print(tuple)
# print(id(tuple))
# print(type(tuple))

# tuple.append('welcome')
# print(tuple)
# print(id(tuple)) #getting Attribute error b/c we can't modify tuples

# sample_list=[1,2.5,"python",[1,2,3],(1,2,3)]
# print(sample_list)

# sample_tuple=(1,2.5,"python",[1,2,3],(1,2,3))
# print(sample_tuple)

#3.Sets--->unordered sequence of elements and allows only immutable datatypes as values,mutable,enclosed in {} and separated with commas
#won't allow duplicates
# set={1,2.5,(1,2,3),"python"}
# print(set)
# print(type(set))

# set={1,2.5,(1,2,3),"python",1,3,6,3}
# print(set)
# print(type(set))

# list=[1,2.5,(1,2,3),"python",1,3,6,3]
# print(list) #lists allow duplicate values
# print(type(list))

# tuple=(1,2.5,(1,2,3),"python",1,3,6,3)
# print(tuple) #tuples allow duplicate values
# print(type(tuple))

# set={1,2.5,(1,2,3),"python",1,3,6,3,{1,2,3}}
# print(set) #Getting type error b/c sets won't allow mutable datatypes as values

#4.Dictionary--->ordered collection of key value pairs,keys must be unique and immutable data types and values allow duplicates,mutable,enclosed in {} and separated with :
# dict={"user1":"user1@123","user2":"user2@123","user3":"user3@123"}
# print(dict)
# print(type(dict))

# dict={"user1":"user1@123","user2":"user2@123","user1":"user3@123"}
# print(dict) #if we use duplicate kay then it will be modify that key value with latest value
# print(type(dict))

# dict={1:1234,2:1234,"word":"text",(1,2,3):24}
# print(dict)
# print(type(dict))

# dict={1:1234,2:1234,"word":"text",[1,2,3]:24}
# print(dict) #Getting type error b/c key we are taking list 
# print(type(dict))

#Complex data type--->used to represent complex numbers i.e it has real part and imaginary part in the form a+bj
# num_1=3+5j
# print(num_1)
# print(type(num_1))

# num_1=3+5j
# num_2=3+6j
# print(num_1+num_2)

#Boolean datatype---> It returns 2 values i.e True(1), False(0)
# sample=True
# print(sample)
# print(type(sample))

# sample=False
# print(sample)
# print(type(sample))

# print(bool(0))
# print(bool(1))

#converting list to tuple
# list=[1,2,3,4,5]
# tuple=tuple(list)
# print(tuple)

#converting tuple to list
# tuple=(1,2,3,4,5)
# list=list(tuple)
# print(list)

#converting list to set and set to list
list_name=[1,2,3,4,5,3,4,1]
set_name=set(list_name)
print(set_name)
print(type(set_name))
list_name_1=list(set_name)
print(list_name_1)
