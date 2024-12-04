a = [1, 3, 5, 7, 4]

# Step 1
print(a[-2])  # Accessing second last element
print(a[2])   # Accessing third element
print(len(a)) # Finding length of the list
print(type(a))# Finding type of the list

# Step 2
a[3] = 50
print(a)      # List after changing the value at index 3
print(a[2:4]) # Slicing the list from index 2 to 3 (4 is exclusive)

# Step 3
a.append(100) # Adding 100 at the last index
a.insert(2, 200) # Adding 200 at index 2
print(a)      # List after additions

# Step 4
a.pop()       # Removing the last element
a.pop(1)      # Removing the element at index 1
print(a)      # List after removals

# Step 5
new_list = [2, 4, 6]
a.extend(new_list) # Joining the new list with a
print(a)           # List after joining

# Step 6
b = a.copy()  # Copying all values to a new list b
print(b)      # New list b

# Step 7
b.sort()      # Sorting the list b
print(b)      # Sorted list b

# Step 8
for element in a:
    print(element)
    if element == 5:
        break

# Step 9
largest = max(a) # Finding the largest number
print(largest)   # Largest number in the list