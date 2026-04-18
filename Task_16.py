"""Problem 1: Using break in a While Loop
Write a Python program that takes a list of numbers as input numbers = [25, 30,
20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds
100, stop adding numbers and print "Sum exceeded 100"."""

# numbers=[25,25,30,40,15,25,65]
# sum=0
# i=0
# while i<len(numbers):
#     sum+=numbers[i]
#     if(sum>100):
#         print(f"last iteration {i}")
#         print(f"last iteration {numbers[i]}")
#         break
#     i+=1
# print(sum)
# print(f"sum exceeded 100")



"""Problem 2: Using continue in a For Loop
Write a Python script that uses a for loop to iterate through numbers from 1 to
600. Print only the odd numbers, skipping the even ones using the continue
statement.
"""

# for i in range(1,601):
#     if(i%2==0):
#         continue
#     print(i)

"""Problem 3: Using pass in Conditional Statements
Write a Python script that checks if a number is even or odd. If the number is
even, print "Even"; if odd, do nothing (use the pass statement)."""

# num_1=int(input("Enter num_1: "))
# if num_1%2==0:
#     print("Even")
# else:
#     pass

"""Problem 4: Combining Transfer Statements
Write a Python script that iterates through a list of words. If the word is "break,"
exit the loop using the break statement. If the word is "skip," skip the rest of the
code for the current iteration using the continue statement. For any other word,
print the word."""

# words_list=["python","skip","ramu","sita","skip","raghav","python","ram","break"]
# for i in words_list:
#     if i!="break" and i!="skip":
#         print(i)
#     elif i=="skip":
#         continue
#     else:
#         break
# print(f"last iteration {i}")