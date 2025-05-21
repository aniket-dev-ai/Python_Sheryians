# Python Built-in Data Structures - Overview

# 1. List
# Ordered, mutable, allows duplicate elements.
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')      # Add element
fruits[1] = 'blueberry'      # Modify element
print(fruits)                # ['apple', 'blueberry', 'cherry', 'orange']

# 2. Tuple
# Ordered, immutable, allows duplicate elements.
coordinates = (10, 20)
print(coordinates[0])   # 10
print(coordinates)   

# 3. Set
# Unordered, mutable, no duplicate elements.
unique_numbers = {1, 2, 3, 2}
print(unique_numbers)        # {1, 2, 3}
unique_numbers.add(4)
print(unique_numbers)        # {1, 2, 3, 4}

# 4. Dictionary
# Unordered (Python 3.7+ maintains insertion order), mutable, key-value pairs.
person = {'name': 'Alice', 'age': 25}
person['city'] = 'New York'
print(person['name'])        # Alice

# 5. String
# Ordered, immutable sequence of characters.
greeting = "Hello, World!"
print(greeting[7:12])        # World

# 6. Range
# Immutable sequence of numbers, commonly used in loops.
for i in range(3):
    print(i)                 # 0 1 2

# 7. Bytes
# Immutable sequence of bytes.
data = bytes([65, 66, 67])
print(data)                  # b'ABC'

# 8. Bytearray
# Mutable sequence of bytes.
mutable_data = bytearray([65, 66, 67])
mutable_data[0] = 68
print(mutable_data)          # bytearray(b'DBC')

# 9. Frozenset
# Immutable version of set.
frozen = frozenset([1, 2, 3, 2])
print(frozen)                # frozenset({1, 2, 3})

# Summary Table
# | Type        | Ordered | Mutable | Duplicates | Example                |
# |-------------|---------|---------|------------|------------------------|
# | list        | Yes     | Yes     | Yes        | [1, 2, 3]              |
# | tuple       | Yes     | No      | Yes        | (1, 2, 3)              |
# | set         | No      | Yes     | No         | {1, 2, 3}              |
# | dict        | No*     | Yes     | Keys: No   | {'a': 1, 'b': 2}       |
# | str         | Yes     | No      | Yes        | "abc"                  |
# | range       | Yes     | No      | Yes        | range(5)               |
# | bytes       | Yes     | No      | Yes        | b'abc'                 |
# | bytearray   | Yes     | Yes     | Yes        | bytearray(b'abc')      |
# | frozenset   | No      | No      | No         | frozenset([1, 2, 3])   |

# *Dictionaries maintain insertion order from Python 3.7+