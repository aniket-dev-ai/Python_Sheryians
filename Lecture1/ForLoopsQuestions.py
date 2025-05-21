# 1. Accept an integer and Print hello world n times
n = int(input("Enter a number: "))
for _ in range(n):
    print("hello world")

# 2. Print natural numbers up to n
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i, end=' ')
print()

# 3. Reverse for loop. Print n to 1
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i, end=' ')
print()

# 4. Take a number as input and print its table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 5. Sum up to n terms
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
print("Sum up to n terms:", total)

# 6. Factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

# 7. Print the sum of all even & odd numbers in a range separately
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
even_sum = 0
odd_sum = 0
for i in range(start, end+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

# 8. Print all the factors of a number
n = int(input("Enter a number: "))
print("Factors:", end=' ')
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
print()

# 9. Accept a number and check if it is a perfect number or not
n = int(input("Enter a number: "))
sum_factors = 0
for i in range(1, n):
    if n % i == 0:
        sum_factors += i
if sum_factors == n:
    print("Perfect number")
else:
    print("Not a perfect number")

# 10. Check whether the number is prime or not
n = int(input("Enter a number: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# 11. Reverse a string without using in-built functions
s = input("Enter a string: ")
rev = ''
for i in range(len(s)-1, -1, -1):
    rev += s[i]
print("Reversed string:", rev)

# 12. Check string is Palindrome or not
s = input("Enter a string: ")
rev = ''
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

# 13. Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
chars = digits = symbols = 0
for ch in str1:
    if ch.isalpha():
        chars += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1
print("Chars =", chars)
print("Digits =", digits)
print("Symbol =", symbols)