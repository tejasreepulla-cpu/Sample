# import datetime
# print(datetime.datetime(2002,6,22,5,20,52,54))

# from datetime import datetime
# print(datetime(2002,6,22,5,20,52,54))

# import datetime
# time1=datetime.timedelta(weeks=2,days=2020)
# time2=datetime.timedelta(weeks=10,days=2015)
# print(time2-time1)

# from datetime import timedelta
# time1=timedelta(weeks=2,days=2020)
# time2=timedelta(weeks=10,days=2015)
# print(time2-time1)

# from functools import partial
# def multiply(x, y):
#     return x * y
# double = partial(multiply, 2)
# print(double(4))

# from functools import partial, Placeholder

# def subtract(a, b):
#     return a - b

# # Use Placeholder to fix the SECOND argument (b) to 10
# # This creates a function: lambda x: subtract(x, 10)
# subtract_ten = partial(subtract, Placeholder, 10)

# print(subtract_ten(50))  # Output: 40 (50 - 10)

# import keyword

# # List all soft keywords in the current Python version
# print("Soft Keywords:", keyword.softkwlist)

# # Check if specific words are soft keywords
# print("'match' is soft keyword:", keyword.issoftkeyword("match"))
# print("'type' is soft keyword:", keyword.issoftkeyword("type"))
# print("'if' is soft keyword:", keyword.issoftkeyword("if"))

# import numbers
# z = complex(3, 5) 
# print(z)
# import numbers

# # Define different numeric types
# x = 10          # Integer
# y = 10.5        # Float
# z = 3 + 4j      # Complex number

# # Check if they are instances of numbers.Real
# print(f"Is {x} a real number? {isinstance(x, numbers.Real)}")   # True
# print(f"Is {y} a real number? {isinstance(y, numbers.Real)}")   # True
# print(f"Is {z} a real number? {isinstance(z, numbers.Real)}")

# import operator
# addition = operator.add(2,3)
# print(addition)

# import os
# current_dir = os.getcwd()
# print(current_dir)

# import os
# print(os.listdir('.'))

# import random
# colors = ["red", "blue", "green", "yellow"]
# print(random.choice(colors))

# import random
# print(random.uniform(10.5, 25.3))

# import time
# print(time.time())

# import time
# print("Start")
# time.sleep(2.5)  # Pauses for 2.5 seconds
# print("End")








