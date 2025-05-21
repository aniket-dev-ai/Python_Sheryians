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
