import random

# Creating a list
my_list = [10, 20, 30, 40, 50]

# 1. append() - Add an element at the end
my_list.append(60)
print("After append:", my_list)

# 2. insert() - Insert at a specific index
my_list.insert(2, 25)
print("After insert:", my_list)

# 3. remove() - Remove first occurrence of a value
my_list.remove(25)
print("After remove:", my_list)

# 4. pop() - Remove and return element at index (default last)
popped = my_list.pop()
print("Popped element:", popped)
print("After pop:", my_list)

# 5. index() - Get index of first occurrence of a value
idx = my_list.index(30)
print("Index of 30:", idx)

# 6. count() - Count occurrences of a value
cnt = my_list.count(20)
print("Count of 20:", cnt)

# 7. sort() - Sort the list
my_list.sort()
print("After sort:", my_list)

# 8. reverse() - Reverse the list
my_list.reverse()
print("After reverse:", my_list)

# 9. copy() - Shallow copy of the list
copy_list = my_list.copy()
print("Copy of list:", copy_list)

# 10. clear() - Remove all elements
copy_list.clear()
print("After clear:", copy_list)

# Traversing a list using for loop
print("Traversing using for loop:")
for item in my_list:
    print(item)



# Print positive and negative elements of the list
print("Positive elements:", [x for x in my_list if x > 0])
print("Negative elements:", [x for x in my_list if x < 0])

# Mean of list elements
if my_list:
    mean = sum(my_list) / len(my_list)
    print("Mean of list elements:", mean)
else:
    print("Mean of list elements: List is empty")

# Find the greatest element and print its index
if my_list:
    greatest = max(my_list)
    idx_greatest = my_list.index(greatest)
    print("Greatest element:", greatest, "at index", idx_greatest)
else:
    print("Greatest element: List is empty")

# Find the second greatest element
if len(my_list) >= 2:
    unique_sorted = sorted(set(my_list), reverse=True)
    if len(unique_sorted) >= 2:
        second_greatest = unique_sorted[1]
        print("Second greatest element:", second_greatest)
    else:
        print("Second greatest element: Not enough unique elements")
else:
    print("Second greatest element: List too small")

# Check if list is sorted or not
is_sorted = all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))
print("List is sorted:" if is_sorted else "List is not sorted.")