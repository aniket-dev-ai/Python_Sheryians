# Python Basics: Comments, Variables, and Data Types

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

### Example Usage

```python
# Examples of data types
name = "Harsh Bhaiya"    # String
age = 25                  # Integer
pi = 3.14159              # Float
is_student = True         # Boolean
numbers = [1, 2, 3, 4, 5] # List
```

Using these conventions and understanding data types ensures clear, efficient, and readable Python code.
