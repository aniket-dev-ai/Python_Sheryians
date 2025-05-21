print(134>100)
print(134<100 and 100>50)
print(134<100 or 100>50)
print(not(134<100 or 100>50))
print(134==100)


# if Else Statement
# if condition:
#     # code to be executed if condition is true
# else:
#     # code to be executed if condition is false

# Example

a = 10
b = 20

if a < b:
    print("a is less than b")
else:
    print("a is greater than or equal to b")

# if Elif Else Statement
# if condition1:
#     # code to be executed if condition1 is true
# elif condition2:
#     # code to be executed if condition2 is true
# else:
#     # code to be executed if both condition1 and condition2 are false

# Example
a = 10
b = 20
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")    
# Nested if Statement
# if condition1:
#     if condition2:
#         # code to be executed if condition1 and condition2 are true
#     else:
#         # code to be executed if condition1 is true and condition2 is false
# else:
#     # code to be executed if condition1 is false
# Example
a = 10
b = 20

if a < b:
    if b > 15:
        print("a is less than b and b is greater than 15")
    else:
        print("a is less than b and b is less than or equal to 15")
else:
    print("a is greater than or equal to b")
    
# Ternary Operator
# # Ternary operator is a shorthand way of writing an if-else statement
# # Ternary operator is also known as conditional expression
print("a is less than b") if a < b else print("a is greater than or equal to b")
# Example
a = 10
b = 20
result = "a is less than b" if a < b else "a is greater than or equal to b"
print(result)
# Example

# Q1. Accept two numbers and print the greatest between them.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")

# Q2. Accept the gender from the user as char and print the respective greeting message
gender = input("Enter your gender (M/F): ").strip().upper()
if gender == 'M':
    print("Good Morning Sir")
elif gender == 'F':
    print("Good Morning Ma'am")
else:
    print("Good Morning")

# Q3. Accept an integer and check whether it is an even number or odd.
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Q4. Accept name and age from the user. Check if the user is a valid voter or not.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hello {name}, you are a valid voter")
else:
    print(f"Hello {name}, you are not a valid voter")

# Q5. Accept a year and check if it is a leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


'''
If- elif ladder
@ You can also create if elif ladder using multiple conditions of
elif.
@ For understanding solve this question
@ take the input of temperature in celsius
@ Below 0°C → "Freezing Cold"
@ 0°C to 10°C → "Very Cold"
@ 10°C to 20°C → "Cold"
@ 20°C to 30°C → "Pleasant"
@ 30°C to 40°C → "Hot"
@ Above 40°C → "Very Hot"
'''

temperature = float(input("Enter temperature in Celsius: "))
if temperature < 0:
    print("Freezing Cold")
elif temperature < 10:
    print("Very Cold")
elif temperature < 20:
    print("Cold")
elif temperature < 30:
    print("Pleasant")
elif temperature < 40:
    print("Hot")
else:
    print("Very Hot")