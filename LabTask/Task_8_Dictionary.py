employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["ios", "android"]},
    "permanent": True,
    "Salary": 30000,
    100: 11213,
    4.5: 5.6,
    True: 7,
    1: 1
}

# 1. Print length, type, and the dictionary
print(len(employee))  # Length of the dictionary
print(type(employee)) # Type of the dictionary
print(employee)       # The dictionary itself

# 2. Access the key employee["type"]["developer"]
print(employee["type"]["developer"])

# 3. Change the value of "permanent" to False
employee["permanent"] = False
print(employee["permanent"])

# 4. Add a new key "gender" having value "male"
employee["gender"] = "male"
print(employee["gender"])

# 5. Remove the "age" key from the dictionary
employee.pop("age")
print(employee)

# 6. Use keys(), values(), items()
print(employee.keys())   # All keys in the dictionary
print(employee.values()) # All values in the dictionary
print(employee.items())  # All key-value pairs in the dictionary

# 7. Iterate the dictionary using a loop
for key, value in employee.items():
    print(f"{key}: {value}")