
"""
Python calculator
"""

import math
import sys

print("Welcome to the Python Calculator!")
num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
if operator == "sqrt":
    print(math.sqrt(num1))
    sys.exit()
elif operator == "abs":
    print(math.fabs(num1))
    sys.exit()
elif operator == "!":
    print(math.factorial(num1))
    sys.exit()
num2 = float(input("Enter second number: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "^":
    print(num1 ** num2)
elif operator == "mod":
    print(num1 % num2)
else:
    print("Invalid Operator. Please enter only +, -, /, *, ^, sqrt, abs, !, mod")
