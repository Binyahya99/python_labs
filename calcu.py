# get first number from user input and convert to float
num1 = float(input("Enter first number: "))

# get second number from user input and convert to float
num2 = float(input("Enter second number: "))

# ask user to choose an operation from +, -, *, /
operation = input("Choose an operation (+, -, *, /): ")

# calculate result based on chosen operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # handle division by zero error
    if num2 == 0:
        result = "Error: Division by zero"
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation"

# display the result to the user
print("Result:", result)
