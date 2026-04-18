# Strings:Immutable,sequence of characters
# sample_1=""
# print(sample_1)
# print(type(sample_1))

# empty_string=str()
# print(empty_string)
# print(type(empty_string))

# sentence='python life'
# print(sentence)
# print(sentence[3])
# print(sentence[8])
# print(sentence[-2])
# print(sentence[-6])

# sentence='pythonlife'
# print(sentence[ : : ])
# print(sentence[ : :-1])

# sentence='pythonlife'
# print(sentence[1:4])
# print(sentence[6:10])
# print(sentence[-9:-6])
# print(sentence[-4: ])
# print(sentence[6:])
# print(sentence[8:5:-1])
# print(sentence[5:1:-1])
# print(sentence[-5:-9:-1])
# print(sentence[-3:-5:-1])
# print(sentence[7:5:-1])

#upper:Returns a copy of the original string with all alphabetic characters converted to uppercase.
# name="Tejasree"
# print(name.upper())

#lower:Returns a copy of the original string with all alphabetic characters converted to lowercase.
# name="TejaSree"
# print(name.lower())

#count:Returns the number of occurrences of the specified substring in the given string.
# gmail="tejasree@gmail.com"
# print(gmail.count('a'))

#strip:Returns a copy of the original string with leading and trailing whitespaces removed.
# first_name=" teja sree "
# print(first_name.strip())

#lstrip:Returns a copy of the original string with leading whitespaces removed.
# first_name=" teja sree"
# print(first_name.lstrip())

#rstrip:Returns a copy of the original string with trailing whitespaces removed.
# first_name="teja sree "
# print(first_name.rstrip())

# split:Splits the string into a list of substrings based on the specified separator.
# words_string="rat,dog,fox,camel"
# print(words_string.split(','))

# words_string="rat,dog,fox,camel"
# print(words_string.split('.'))

# products_cost="25,20,45,67,82"
# print(products_cost.split(","))

# length: Returns the number of characters (length) in the given string.
# sentence="python is easy language to learn"
# print(len(sentence))

"""replace:Returns a copy of the original string with occurrences of the specified "old" substring replaced
with the "new" substring."""
# sentence="python is fun!"
# print(sentence.replace("fun","awesome"))

# sentence="python is fun! python is awesome"
# print(sentence.replace("python","Pythonlife"))

# sentence="python    is fun!    python is awesome"
# print(sentence.replace("    "," "))

#startswith:Returns True if the string starts with the specified prefix.
# gmail="tejasree@gmail.com"
# print(gmail.startswith("teja"))
# print(gmail.startswith("sree"))

#endswith:Returns True if the string ends with the specified suffix.
# gmail="tejasree@gmail.com"
# print(gmail.endswith(".com"))
# print(gmail.endswith("sree"))

# email_list=["example1@gmail.com","example2@yahoo.com","example3@outlook.com","example4@gmail.com"]
# gmail_list=[]
# for i in email_list:
#     if i.endswith("@gmail.com"):
#         gmail_list.append(i)
# print(gmail_list)

# email_list=["example1@gmail.com","example2@yahoo.com","example3@outlook.com","example4@gmail.com"]
# gmail_list=[i for i in email_list if i.endswith("@gmail.com")]
# print(gmail_list)

# email_list=["example1@gmail.com","example2@yahoo.com","example3@outlook.com","example4@gmail.com"]
# print([i for i in email_list if i.endswith("@gmail.com")])

"""find:Returns the lowest index of the first occurrence of the specified substring. Returns -1 if the substr
ing is not found."""
# text="python is easy to learn"
# print(text.find('o'))

# text="python is easy to learn"
# print(text.find('z'))

"""index:Returns the lowest index of the first occurrence of the specified substring. Raises a ValueError if
the substring is not found."""

# text="python is easy to learn"
# print(text.index('o'))

# text="python is easy to learn"
# print(text.index('z'))

#capitalize:Returns a copy of the original string with its first character capitalized.
# text="python programming"
# print(text.capitalize())

#isdigit:Returns True if all characters in the string are digits.
# number_string="1234"
# alpha_string="abcde"
# print(number_string.isdigit())
# print(alpha_string.isalpha())

# number_string="123 4"
# alpha_string="abcde"
# print(number_string.isdigit())
# print(alpha_string.isalpha())

# number_string="123.4"
# alpha_string="abcde"
# print(number_string.isdigit())
# print(alpha_string.isalpha())

# number_string="1234"
# alpha_string="abcd e"
# print(number_string.isdigit())
# print(alpha_string.isalpha())

#join:Concatenates the elements of an iterable(e.g., a list) into a single string, using the specified separator
# words_list=["apple","banana","chiku"]
# print(' '.join(words_list))

#format strings:allows you to create dynamic strings by inserting values into placeholders.
# name=input("enter name: ")
# print(f"my name is {name}")


        