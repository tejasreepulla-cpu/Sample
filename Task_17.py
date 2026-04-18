# Data structures:
# 1.list:ordered collection of elements,mutable,allows duplicates, it allows list inside lists 
# and we perform differenet operations like slicing,accessing etc

list_1=[]
print(list_1)
print(type(list_1))

list_2=[5,4.5,"python",(1,2,3),[3,4,5],True]
print(list_2)
print(type(list_2))

list_3=[]
print(list_3)
print(type(list_3))

my_list=[10,20,30,40,50]
print(my_list[2])
print(my_list[4])
print(my_list[0])
print(my_list[-5])
print(my_list[-1])
print(my_list[-3])

my_list=[10,20,30,40,50,60,70,80]
print(my_list[1:4])
print(my_list[5:7])
print(my_list[2:8])
print(my_list[0:8])
print(my_list[ : :])
print(my_list[ : :1])
print(my_list[ : :2])
print(my_list[ : :5])

my_list=[10,20,30,40,50,60,70,80]
print(my_list[1:4])
print(my_list[4:7])
print(my_list[-7:-4])
print(my_list[-4:-1])
print(my_list[-8:-1])
print(my_list[-8: ])

my_list=[10,20,30,40,50,60,70,80]
print(my_list[: :-1])
print(my_list[ : :-2])
print(my_list[ : :-3])
print(my_list[6:3:-1])
print(my_list[1: :-1])
print(my_list[7:4:-1])
print(my_list[1:0:-1])
print(my_list[-8: ])

my_list=[10,20,30,40,50,60,70,80]
print(my_list[: :-1])
print(my_list[5:2:-1])
print(my_list[-3:-6:-1])
print(my_list[-6: :-1])
print(my_list[-2:-4:-1])

#Nested list:list inside another list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][1])
print(matrix[2][2])
print(matrix[0][2])
print(matrix[1][0])
