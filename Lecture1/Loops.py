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