#Transfer Statements:
#1.Break:used to exit the loop permanently
# Syntax:
# for item in iterable:
#     if condition:
#         break

# for i in range(10):
#     print(i)

# for i in range(10):
#     if(i==3):
#         print(i)
# print(f"last iteration {i}")

# for i in range(10):
#     if(i==3):
#         print(i)
#         break
# print(f"last iteration {i}")

# voter_data=["ramu","sita","ravi","gita"]
# for i in voter_data:
#     if(i=="raju"):
#         print(i)
#         break
# print(f"last iteration {i}")

"""2.continue:it skips the current iteration and continues the next iteration
syntax:
for item in iterable:
    if condition:
        continue
    # code here will be skipped if the condition is met"""
    
# products_data=['ok','ok','ok','ok','defect','ok','defect','ok','ok']
# for i in products_data:
#     if i=='defect':
#         break
#     print(i)
# print(f"last iterator {i}")

# products_data=['ok','ok','ok','ok','defect','ok','defect','ok','ok','defect']
# for i in products_data:
#     if i=='defect':
#         continue
#     print(i)
# print(f"last iterator {i}")

# for i in range(1,10):
#     if(i%2==0):
#         print(i)

# for i in range(1,10):
#     if(i%2==0):
#         continue
#     print(i)

# name="tejasree"
# for i in name:
#     if i in "aeiou":
#         print(i)

# name="tejasree"
# for i in name:
#     if i in "aeiou":
#         continue
#     print(i)

#3.pass:It is a null operation which means it won't do anything
# num_1=35
# if num_1>=18:
#     print(num_1+10)

# num_1=35
# if num_1>=18:
#     pass

# for i in range(10):
#     pass
# print(f"last iteration {i}")

