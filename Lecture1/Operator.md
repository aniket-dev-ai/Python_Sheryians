# Python Basics: Comments, Variables, Data Types, and Operators

## Comments

Comments in Python are used to explain the code and make it easier to read. Python supports single-line and multi-line comments.

### Single-Line Comments

Use `#` to denote single-line comments.

```python
# This is a single-line comment
```

### Multi-Line Comments

Multi-line comments can be enclosed within triple quotes (`"""`).

```python
"""
This is a multi-line comment.
Useful for detailed explanations.
"""
```

## Variables

Variables store data that can be used and manipulated by a program. Python has specific rules for naming variables:

* Variable names can contain letters, numbers, and underscores (`_`).
* Variable names **cannot** start with a number.
* Variable names **cannot** contain spaces.
* Variable names **cannot** be Python reserved keywords (e.g., `def`, `return`, `if`, `else`, etc.).
* Variable names are **case-sensitive** (`var` and `Var` are different).
* Variable names should be descriptive to improve code readability.

### Examples

```python
# Descriptive variable
user_name = "Harsh Bhaiya"

# Naming conventions
myVariable = "Hello World"  # CamelCase
my_variable = "Hello World"  # snake_case (recommended)
MyVariable = "Hello World"  # PascalCase

# Using a variable
print(MyVariable)
```

## Data Types

Data types specify the kind of data that variables can hold. Python has several fundamental data types:

| Data Type | Description                           | Example           |
| --------- | ------------------------------------- | ----------------- |
| String    | A sequence of characters              | `"Hello World"`   |
| Integer   | A whole number (positive or negative) | `42`              |
| Float     | A decimal number                      | `3.14`            |
| Boolean   | Represents `True` or `False`          | `True`, `False`   |
| List      | A collection of ordered values        | `[1, 2, 3, 4, 5]` |

### String Details

Strings occupy more memory because each character is encoded using Unicode, which assigns a unique numerical value to every character (e.g., `A` = 65, `a` = 97).

```python
# Unicode example
a = 65
print(a)
print(chr(a))  # Output: A

# String indexing (starts from 0, negative indexing from -1)
a = "Hello "
print(a[0])  # H
print(a[1])  # e
print(a[2])  # l
print(a[3])  # l
print(a[4])  # o
print(a[5])  # space

# String slicing
print(a[0:3])  # Hel
print(a[0:])   # Hello
```

## Type Conversion

Type conversion is changing one data type into another. Python supports implicit and explicit conversions.

### Implicit Type Conversion

Automatically performed by Python.

```python
a = 12
b = 3.14
c = a + b
print(c)  # 15.14
```

### Explicit Type Conversion

Manually performed by the programmer.

```python
a = 12
b = 3.14
c = a + int(b)
print(c)  # 15
```

### Falsy and Truthy Values

* **Falsy values** evaluate to `False`: `0`, `""`, `[]`, `{}`, `None`
* **Truthy values** evaluate to `True`: `1`, `"Hello"`, `[1, 2, 3]`, `{"name": "John"}`, `True`

```python
# Example
if "":
    print("Truthy")
else:
    print("Falsy")  # Output: Falsy
```

## Operators

Operators are special symbols that perform operations on variables and values. Python follows the BODMAS rule (Brackets, Order, Division, Multiplication, Addition, Subtraction).

### Arithmetic Operators

Perform basic mathematical operations:

```python
a = 10
b = 20

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division
```

### Comparison Operators

Used to compare two values:

```python
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
```

### Assignment Operators

Assign and modify variable values:

```python
a = 10
b = 20
a += b  # Equivalent to a = a + b
print(a)
```

### Logical Operators

Evaluate logical expressions:

```python
print(a and b)  # Logical AND
print(a or b)   # Logical OR
print(not a)    # Logical NOT
```

### Identity Operators

Check if two variables point to the same object:

```python
print(a is b)      # Identity is
print(a is not b)  # Identity is not
```
