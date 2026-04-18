# List methods:
#1.append:add element at the end of the list with any datatype
# list1=[10,20,30,40,50]
# list1.append(35)
# list1.append("python")
# print(list1)

# list1=[10,20,30,40,50]
# list1.append("pythonlife",15,25)
# print(list1)  #TypeError

#2.extend: used to extend the existing list
# list1=[10,20,30,40,50]
# list2=[60,70,80]
# list1.extend(list2)
# print(list1)

#3.copy:returns the shallow copy of the list
# list1=[10,20,30,40,50]
# list2=list1.copy()
# print(list2)
# list2.append("ram")
# print(list2)
# print(list1)

#4.clear:removes all the elements from the list
# list1=[10,20,30,40,50]
# list1.clear()
# print(list1)

#5.count:used to get the no of times specific item repeated
# list1=[10,20,30,40,50,10,11,10]
# print(list1.count(10))

# 6.index:returns index of the first occurence of a specified item in the list
# list1=[10,20,30,40,30,50,10,11,10]
# print(list1.index(30))
# print(list1.index(50))
# print(list1.index(10))

# 7.remove:removes the first occurence of a specified item in the list
# list1=[10,20,30,40,30,50,10,11,10]
# list1.remove(30)
# print(list1)
# list1.remove(10)
# print(list1)

# 8.pop:it removes element at particular index
# list1=[10,20,30,40,30,50,10,11,10]
# pop_number=list1.pop(2)
# print(list1)
# print(pop_number)
# print(pop_number*5)

# 9.insert:used to insert a element at particular position
# list1=[10,20,30,40,30]
# list1.insert(2,45)
# print(list1)

# 10.reverse:reverse the elemants of the list
# list1=[10,20,30,40,30]
# list1.reverse()
# print(list1)

#11.sort:used to sort the elements in the ascending or descending order
# list1=[10,40,30,20,30]
# list1.sort()
# print(list1)

# list1=[10,40,30,20,30]
# list1.sort(reverse=True)
# print(list1)

# List Comprehension:provide concise way to create list
# syntax:[exp for item in iteration if condition]

# for i in range(10):
#     if i%2==0:
#         print(i)
# print(type(i))

# empty_list=[]
# for i in range(11):
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# for i in range(11):
#     result=i**2
#     print(result)

# empty_list=[]
# for i in range(11):
#     result=i**2
#     empty_list.append(result)
# print(empty_list)

# result=[i**2 for i in range(11)]
# print(result)

# print([i**2 for i in range(11)])

# result=[i for i in range(11) if i%2==0]
# print(result)

# print([i for i in range(11) if i%2==0])

# remove:
# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4]
# list1.remove(1)
# print(list1)

# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4]
# for i in list1:
#     if i==4:
#         list1.remove(i)
# print(list1)

# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4]
# list2=[]
# for i in range(len(list1)):
#     if(list1[i]!=4):
#         list2.append(list1[i])
# print(list2)

# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4]
# list2=[]
# for i in list1:
#     if(i!=4):
#         list2.append(i)
# print(list2)

# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4]
# print([i for i in list1 if i!=4])

# index:
# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4,48,7,3,3,4,7,4,8,9,4,9,3,9,4,4,4,7,4,3,8,4,9,3,4,7,3,4,7,5,4,8,4,9,4,6,5,4,5,4,5,6,4,7,4,7,4,8,4,9,4,3,4]
# print(list1.index(4))

# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4]
# list2=[]
# for i in range(len(list1)):
#     if list1[i]==4:
#         list2.append(i)
# print(list2)

# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4]
# print([i for i in range(len(list1)) if list1[i]==4])
        
# list1=[1,4,2,5,7,4,8,2,9,3,8,3,9,44,278,48,7,3,3,4,7,4,8,9,4]
# print(len(list1)) 

# list1=[1,2,3,4]
# list2=[5,6,7]
# print(list1+list2)

# list1=[5,6,7]
# print(list1*3)

#Real time example:
# user_data=[]
# length=int(input("enter length: "))
# for i in range(length):
#     user_name=input("enter user_name: ")
#     user_data.append(user_name)
# print(user_data)

# user_data=[]
# while True:
#     user_name=input("enter user_name: ")
#     user_data.append(user_name)
#     if user_name=='Stop':
#         break
# print(user_data)
    



        