# Dictionary:Collection of key value pairs,mutable,ordered
# Keys allow only immutable datatypes and it won't allow duplicates 
# values allow any type of datatypes and it will allow duplicates

# dict_1={}
# print(dict_1)
# print(type(dict_1))

# dict_1=dict()
# print(dict_1)
# print(type(dict_1))

# dict_1={1:"vasu",2:"krishna",3:"raju"}
# print(dict_1)
# print(len(dict_1))

# dict_1={1:"vasu",2:"krishna",3:"raju",(1,2,3):123,"name":"raj"}
# print(dict_1)
# print(len(dict_1))

# dict_1={1:"vasu",2:"krishna",3:"raju",(1,2,3):{1,2,3},"name":"raj",4:{1:"raj",}}
# print(dict_1)
# print(len(dict_1))

# dict_1={1:"vasu",2:"krishna",1:"raju"}
# print(dict_1)

# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# print(dict_1)

# Dictionary methods:
# 1.clear:used to remove all the items from the dictionary
# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# dict_1.clear()
# print(dict_1)

# 2.copy:reurns the copy of the original dictionary/shallow copy of the original dictionary
# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# dict_2=dict_1.copy()
# print(dict_2)
# dict_2.clear()
# print(dict_2)
# print(dict_1)

# 3.items:returns a list containing a tuple for each key value pairs
# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# print(dict_1.items())

# 4.keys:returns a list containing keys of the dictionary
# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# print(dict_1.keys())

# 5.values:returns a list contaning the values of the dictionary
# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# print(dict_1.values())

# 6.update:used to update items from one dictionary to another dictionary
# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# dict_2={5:"123",6:"abc"}
# print(dict_1.update(dict_2))
# print(dict_1)
# print(dict_2)

# 7.get:used to access the values of a particular key
# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# print(dict_1.get(2))
# print(dict_1.get(5))  #returning None

# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# print(dict_1[3])
# print(dict_1[5])    #returning Key error

# 8.pop:to remove particular value from the dictionary and we can store that pop value
# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# print(dict_1.pop(2))
# print(dict_1)

# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# obj=dict_1.pop(2)
# print(obj)

# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# dict_1[5]="ramu"
# print(dict_1)

# dict_1={1:"vasu",2:"krishna",3:"raju",4:"vasu"}
# dict_1[2]=[1,2,3]
# print(dict_1)

# user=input("Enter user: ")
# password=input("Enter password: ")
# dict_1={}
# dict_1[user]=password
# print(dict_1)

