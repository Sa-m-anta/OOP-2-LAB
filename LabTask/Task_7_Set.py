a = {1, 3, 5, 8, 77}
b = {0, False, 1, 5}

# 1. Print a, b
print(a)
print(b)

# 2. Print length and their type
print(len(a))
print(type(a))
print(len(b))
print(type(b))

# 3. Add a new element 10 in set a
a.add(10)
print(a)

# 4. Remove 8 from the set a
a.remove(8)
print(a)

# 5. Perform union, intersection, difference, symmetric difference, and subset operations on set a and set b
union_set = a.union(b)
intersection_set = a.intersection(b)
difference_set = a.difference(b)
symmetric_difference_set = a.symmetric_difference(b)
is_subset = a.issubset(b)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
print("Is Subset:", is_subset)

# 6. Join a new list [2, 3, 4] with set a
new_list = [2, 3, 4]
a.update(new_list)
print(a)