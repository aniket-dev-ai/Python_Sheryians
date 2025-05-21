# 1. Simple function (no parameters, no return value)
def greet():
    # This function just prints a greeting message
    print("Hello, welcome to Python functions!")

# 2. Function with parameters (no return value)
def greet_person(name):
    # This function takes a parameter and prints a personalized greeting
    print(f"Hello, {name}!")

# 3. Function with parameters and return value
def add(a, b):
    # This function takes two numbers and returns their sum
    return a + b

# 4. Function with default parameters
def power(base, exponent=2):
    # This function returns base raised to the power of exponent
    return base ** exponent

# 5. Function with variable number of positional arguments (*args)
def sum_all(*args):
    # This function sums any number of arguments
    return sum(args)

# 6. Function with variable number of keyword arguments (**kwargs)
def print_info(**kwargs):
    # This function prints key-value pairs passed as keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 7. Lambda function (anonymous function)
multiply = lambda x, y: x * y  # Multiplies two numbers

# 8. Recursive function (calls itself)
def factorial(n):
    # This function returns the factorial of n
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usages:
greet()
greet_person("Aniket")
print(add(3, 5))
print(power(3))
print(power(3, 3))
print(sum_all(1, 2, 3, 4, 5))
print_info(name="Aniket", age=19, city="Kanpur, Uttar Pradesh")
print(multiply(4, 5))
print(factorial(5))