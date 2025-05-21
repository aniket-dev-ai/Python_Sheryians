'''
Operators in Python
Operators are special symbols that perform operations on variables and values
'''


# BODMAS rule = Brackets, Order, Division, Multiplication, Addition, Subtraction

a = 10 
b = 20

# Arithmetic Operators

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division


# Comparison Operators
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to


# Assignment Operators
a = 10
b = 20
a += b  # a = a + b
print(a)  # 30
a -= b  # a = a - b
print(a)  # 10
a *= b  # a = a * b
print(a)  # 200
a /= b  # a = a / b
print(a)  # 10.0
a %= b  # a = a % b
print(a)  # 10.0
a **= b  # a = a ** b
print(a)  # 100
a //= b  # a = a // b
print(a)  # 5.0

# Logical Operators
print(a and b)  # Logical AND
print(a or b)  # Logical OR
print(not a)  # Logical NOT

# Identity Operators
print(a is b)  # Identity is
print(a is not b)  # Identity is not