# Program name: Calculator
# Program description: Calulates given 2 integers and an operator
# Author: Saran Wagner
# Date: January 10 2023

# Asks user for 2 integers and an operator
num1 = int(input("Enter an integer (the order of the number matters)"))
num2 = int(input("Enter another integer (the order of the number matters)"))
operator = input("Enter an operator")

# Addition function defined
def addition(num1, num2):
    return num1 + num2

# Subtraction function defined
def subtraction(num1, num2):
    return num1 - num2

# Multiplication function defined
def multiplication(num1, num2):
    return num1 * num2

# Division function defined
def division(num1, num2):
    return num1 / num2

# If statements to call functions
if operator == "+":
    result = addition(num1, num2)
elif operator == "-":
    result = subtraction(num1, num2)
elif operator == "*":
    result = multiplication(num1, num2)
elif operator == "/":
    result = division(num1, num2)

# Prints result
print(result)
