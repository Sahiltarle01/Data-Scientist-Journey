# Python Day 4 Assignment
# Q1. Print Numbers from 1 to 100
print("Q1. Numbers from 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# Q2. Print Numbers from 100 to 1
print("Q2. Numbers from 100 to 1")
for i in range(100, 0, -1):
    print(i, end=" ")
print("\n")

# Q3. Print Even Numbers
print("Q3. Even Numbers (1-100)")
for i in range(2, 101, 2):
    print(i, end=" ")
print("\n")

# Q4. Print Odd Numbers
print("Q4. Odd Numbers (1-100)")
for i in range(1, 100, 2):
    print(i, end=" ")
print("\n")

# Q5. Multiplication Table
print("Q5. Multiplication Table")
num = int(input("Enter Number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Q6. Sum of First N Natural Numbers
print("\nQ6. Sum of First N Natural Numbers")
n = int(input("Enter N: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =", sum)

# Q7. Factorial
print("\nQ7. Factorial")
num = int(input("Enter Number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial =", factorial)

# Q8. Count Digits
print("\nQ8. Count Digits")
number = int(input("Enter Number: "))
count = 0
temp = number
while temp > 0:
    temp //= 10
    count += 1
print("Total Digits =", count)

# Q9. Reverse Number
print("\nQ9. Reverse Number")
number = int(input("Enter Number: "))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10
print("Reverse =", reverse)

# Q10. Star Pattern
print("\nQ10. Star Pattern")
for i in range(1, 6):
    print("*" * i)

# Q11. Print Alphabets A-Z
print("\nQ11. Alphabets")
for i in range(65, 91):
    print(chr(i), end=" ")
print("\n")

# Q12. Print Squares from 1 to 10
print("Q12. Squares")
for i in range(1, 11):
    print(f"{i} Square = {i*i}")

# Q13. Print Cubes from 1 to 10
print("\nQ13. Cubes")
for i in range(1, 11):
    print(f"{i} Cube = {i**3}")

# Q14. Simple Number Guess Loop
print("\nQ14. Guess Number")
secret = 7
guess = int(input("Guess the Number (1-10): "))
while guess != secret:
    print("Wrong Guess! Try Again.")
    guess = int(input("Guess Again: "))
print("Congratulations! You guessed correctly.")

# Q15. Mini Menu
print("\nQ15. Menu Program")
while True:
    print("\n===== MENU =====")
    print("1. Say Hello")
    print("2. Print Your Name")
    print("3. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("Hello Sahil!")
    elif choice == 2:
        print("Name: Sahil Shantaram Tarle")
    elif choice == 3:
        print("Program Ended.")
        break
    else:
        print("Invalid Choice!")
