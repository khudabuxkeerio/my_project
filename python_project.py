# Simple calculator in Python

print("Simple Calculator")
print("Operations: +, -, *, /")

num1 = float(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero")
        result = None
else:
    print("Error: Invalid operator")
    result = None

if result is not None:
    print("Result:", result)

# i have finished the code for a simple calculator in Python. It takes two numbers and an operator as input, performs the corresponding arithmetic operation, and displays the result. It also handles division by zero and invalid operators.