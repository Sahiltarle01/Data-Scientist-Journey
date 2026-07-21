#   Exception Handling & Modules
# Q.1 Handle ZeroDivisionError using try and except
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
#  Q.2 Handle ValueError using try and except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Please enter a valid integer.")

# Q.3 Use try, except, and finally
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
finally:
    print("Program execution completed.")
    
# Q.4 Handle multiple exceptions
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Program execution completed.")
    
# Q.5 Raise a custom exception if age is less than 18
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise Exception("You must be at least 18 years old.")
    print("Access granted.")
except ValueError:
    print("Error: Please enter a valid age.")
except Exception as e:
    print("Custom Exception:", e)
    
# Q.6 Import the math module
import math
num = float(input("Enter a number: "))
result = math.sqrt(num)
print("Square root =", result)

# Q.7 Use the random module to generate a random number between 1 and 100.
import random
number = random.randint(1, 100)
print("Random Number:", number)

# Q.8 Import the datetime module
import datetime
current = datetime.datetime.now()
print("Current Date and Time:", current)

# Q.9 Create your own module named calculator.py with functions:
# Addition, Subtraction, Multiplication, Division, calculator.py
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

# Import the calculator module
import calculator
print("Addition:", calculator.addition(10, 5))
print("Subtraction:", calculator.subtraction(10, 5))
print("Multiplication:", calculator.multiplication(10, 5))
print("Division:", calculator.division(10, 5))

# Q.10 Create a menu-driven calculator using your custom calculator module.
# calculator.py
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
# main.py
import calculator
print("===== MENU DRIVEN CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == 1:
    print("Result:", calculator.addition(num1, num2))
elif choice == 2:
    print("Result:", calculator.subtraction(num1, num2))
elif choice == 3:
    print("Result:", calculator.multiplication(num1, num2))
elif choice == 4:
    if num2 != 0:
        print("Result:", calculator.division(num1, num2))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid Choice!")