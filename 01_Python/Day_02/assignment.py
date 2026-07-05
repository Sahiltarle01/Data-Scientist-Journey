
# Python Day 2 Assignment

# Q1. Arithmetic Operations
print("Q1. Arithmetic Operations")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)

# Q2. Area of Rectangle
print("\nQ2. Area of Rectangle")
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
area = length * width
print("Area of Rectangle =", area)

# Q3. Area of Circle
print("\nQ3. Area of Circle")
radius = float(input("Enter Radius: "))
circle_area = 3.14 * radius ** 2
print("Area of Circle =", circle_area)

# Q4. Type Casting
print("\nQ4. Type Casting")
string_num = "100"
print("Before:", string_num, type(string_num))
int_num = int(string_num)
print("After String to Integer:", int_num, type(int_num))
integer = 50
print("Before:", integer, type(integer))
float_num = float(integer)
print("After Integer to Float:", float_num, type(float_num))
decimal = 25.5
print("Before:", decimal, type(decimal))
string_value = str(decimal)
print("After Float to String:", string_value, type(string_value))

# Q5. Comparison Operator
print("\nQ5. Comparison Operator")
print("20 > 15 =", 20 > 15)

# Q6. Pass or Fail
print("\nQ6. Pass or Fail")
marks = int(input("Enter Marks: "))
print("Passed =", marks >= 35)

# Q7. Voting Eligibility
print("\nQ7. Voting Eligibility")
age = int(input("Enter Age: "))
print("Eligible to Vote =", age >= 18)

# Q8. Membership Operator
print("\nQ8. Membership Operator")
languages = ["Java", "Python", "C++", "SQL"]
print("Python" in languages)

# Q9. Equality Check
print("\nQ9. Equality Check")
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print("Are both numbers equal?", a == b)

# Q10. Mini Calculator
print("\nQ10. Mini Calculator")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
else:
    print("Division by zero is not possible.")
