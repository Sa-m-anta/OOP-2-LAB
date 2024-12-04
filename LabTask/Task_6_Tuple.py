a = (1, 3, 5, 7, 4)

# a) Find the sum of all odd numbers in a
sum_odd = sum(x for x in a if x % 2 != 0)
print(sum_odd)  # Output: 16

# b) Find the element at index 11 in a
try:
    print(a[11])
except IndexError:
    print("Index out of range")

# c) Count the number of odd and even numbers separately
odd_count = sum(1 for x in a if x % 2 != 0)
even_count = sum(1 for x in a if x % 2 == 0)
print(f"Odd count: {odd_count}, Even count: {even_count}")

# d) Extend the tuple with (2, 4, 6)
a_extended = a + (2, 4, 6)
print(a_extended)

# e) Add a new item at index 2 (400)
a_list = list(a)
a_list.insert(2, 400)
a = tuple(a_list)
print(a)

# f) Remove the last element
a_list = list(a)
a_list.pop()
a = tuple(a_list)
print(a)

# g) Perform slicing [-4:-1]
sliced = a[-4:-1]
print(sliced)

# h) Print the tuple using a loop and use continue if you get 5
for element in a:
    if element == 5:
        continue
    print(element)