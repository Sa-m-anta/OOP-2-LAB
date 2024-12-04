# Taking input
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Lambda function for the same formula
lambda_formula = lambda a, b: (a + b)**2

print("Result using lambda function:", lambda_formula(a, b))