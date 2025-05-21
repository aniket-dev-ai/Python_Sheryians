# loops
for i in range(5):
    print(i)

a = range(1,5,1)
print(a)
for i in a:
    print(i)

b = range(16, 1, -1)    
print(b)

for i in b:
    print(i)
    
# Printing table of Input

a = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{a} x {i} = {a*i}")
    
    # or
    
for i in range(a, a*11, a):
    print(i)
    
a = "Gpt ne life and coding dono kharab kar diya"

for i in range(len(a)):
    print(a[i])
    
    # Continue and Break
# Continue statement is used to skip the current iteration and move to the next iteration
# Break statement is used to exit the loop

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    
# Example
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
    
    
    
    
    
# While Loop
# While loop is used to execute a block of code repeatedly as long as the condition is true
# While loop is used when the number of iterations is not known
i = 1
while i <= 10:
    print(i)
    i += 1
# Example
# Print the sum of first n natural numbers
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum:", sum)