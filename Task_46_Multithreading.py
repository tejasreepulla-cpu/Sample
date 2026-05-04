# Multithreading:

# def squares(numbers):
#     print(f"squares of numbers")
#     for i in numbers:
#         print(f"square of {i} is {i**2}")
# list1=[1,2,3,4,5]
# squares(list1)

# def cubes(numbers):
#     print(f"cubes of numbers")
#     for i in numbers:
#         print(f"cube of {i} is {i**3}")
# list1=[1,2,3,4,5]
# cubes(list1)

# import time
# def squares(numbers):
#     print(f"squares of numbers")
#     for i in numbers:
#         print(f"square of {i} is {i**2}")
#         time.sleep(0.2)
# initial_time=time.time()
# list1=[1,2,3,4,5]
# squares(list1)
# print(f"Time taken is {time.time()-initial_time}")

# def cubes(numbers):
#     print(f"cubes of numbers")
#     for i in numbers:
#         print(f"cube of {i} is {i**3}")
#         time.sleep(0.2)
# initial_time=time.time()
# list1=[1,2,3,4,5]
# cubes(list1)
# print(f"Time taken is {time.time()-initial_time}")

# import threading
# import time
# def squares(numbers):
#     print(f"squares of numbers")
#     for i in numbers:
#         print(f"square of {i} is {i**2}")
#         time.sleep(0.2)
# def cubes(numbers):
#     print(f"cubes of numbers")
#     for i in numbers:
#         print(f"cube of {i} is {i**3}")
#         time.sleep(0.2)
# initial_time=time.time()
# list1=[1,2,3,4,5]
# t1=threading.Thread(target=squares,args=(list1,))
# t2=threading.Thread(target=cubes,args=(list1,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()



