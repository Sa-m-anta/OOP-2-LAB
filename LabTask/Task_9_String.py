a = "hello"
b = "b2b2b2"
c = "3939"

# 1. Declare a new variable d and concatenate a, b, c
d = a + b + c
print(d)  # Output: "hellob2b2b23939"

# 2. Find the length of d and print d[:-3]
length_d = len(d)
print(length_d)  # Output: 15
print(d[:-3])    # Output: "hellob2b2b239"

# 3. Check if "a2" is present in d
is_present = "a2" in d
print(is_present)  # Output: False

# 4. Perform the following operations
print(d.upper())          # Convert to uppercase
print(d.lower())          # Convert to lowercase
print(d.title())          # Convert to title case
print(d.strip())          # Strip whitespace from both ends
print(d.isdigit())        # Check if all characters are digits
print(d.find("3g"))       # Find the substring "3g"
print(d.capitalize())     # Capitalize the first character
print(d.isalnum())        # Check if all characters are alphanumeric
print(d.count("b2"))      # Count occurrences of "b2"
print(d.split())          # Split the string into a list
print(d.swapcase())       # Swap case of all characters
print(d.lstrip())         # Strip whitespace from the left end
print(d.replace("hello", "python"))  # Replace "hello" with "python"