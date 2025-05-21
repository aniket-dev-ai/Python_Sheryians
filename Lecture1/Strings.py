#String Occupies more space than any other data type because it is a collection of character & each character has its own UNICODE value
#Unicode is a standard for encoding characters that has a unique number for every character
# Like A = 65 and a = 97 and 😊 = 12
# # String is a sequence of characters
# # String is a collection of characters

#String indexing starts from 0 and has -1 indexing

a = 65
print(a)
print(chr(a))

a = "Hello "
print(a)
print(a[0])  # H
print(a[1])  # e    
print(a[2])  # l
print(a[3])  # l
print(a[4])  # o
print(a[5])  # space 

print(a[0:3])  # Hel
print(a[0:])  # Hello

# Type Conversion

a = 12
print(type(a))  # <class 'int'>
a = str(a)
print(a)  # 12
print(type(a))  # <class 'str'>

# Falsy values
# Falsy values are values that evaluate to false in a boolean context
# Falsy values are: 0, "", [], {}, None
# Truthy values are values that evaluate to true in a boolean context
# Truthy values are: 1, "Hello", [1, 2, 3], {"name": "John"}, True


# #  Implicit Type Conversion
# # Implicit type conversion is the automatic conversion of one data type to another 
# # Implicit type conversion is done by the Python interpreter
# # Implicit type conversion is done when the operands are of different data types

# # Example of implicit type conversion
a = 12
b = 3.14
c = a + b

print(c)  # 15.14

# # Explicit Type Conversion
# # Explicit type conversion is done by the programmer
# # Explicit type conversion is the manual conversion of one data type to another    

# # Example of explicit type conversion
a = 12
b = 3.14
c = a + int(b)  # Explicit type conversion
print(c)  # 15


