# Simple Calculator
# CodeOrbit Tech - Python Programming Internship

print("===== SIMPLE CALCULATOR =====")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            exit()
        result = num1 / num2
    else:
        print("Invalid operator.")
        exit()

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numbers only.")