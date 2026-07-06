# Python Day 3 Assignment

# Q1. Positive, Negative or Zero
print("Q1. Positive, Negative or Zero")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Q2. Even or Odd
print("\nQ2. Even or Odd")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Q3. Voting Eligibility
print("\nQ3. Voting Eligibility")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Q4. Grade Calculator
print("\nQ4. Grade Calculator")
marks = float(input("Enter your marks: "))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

# Q5. Greater of Two Numbers
print("\nQ5. Greater of Two Numbers")
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
if a > b:
    print(a, "is Greater")
else:
    print(b, "is Greater")

# Q6. Greatest of Three Numbers
print("\nQ6. Greatest of Three Numbers")
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if a >= b and a >= c:
    print(a, "is Greatest")
elif b >= a and b >= c:
    print(b, "is Greatest")
else:
    print(c, "is Greatest")

# Q7. Leap Year
print("\nQ7. Leap Year")
year = int(input("Enter Year: "))
if year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

# Q8. Divisible by 5 and 11
print("\nQ8. Divisible by 5 and 11")
num = int(input("Enter Number: "))
if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible by both 5 and 11.")
else:
    print(num, "is not divisible by both 5 and 11.")

# Q9. Login System
print("\nQ9. Login System")
username = input("Enter Username: ")
password = input("Enter Password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")

# Q10. Mini ATM Project
print("\nQ10. Mini ATM")
balance = 5000
print("\n====== ATM MENU ======")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Your Balance is:", balance)
elif choice == 2:
    amount = float(input("Enter Deposit Amount: "))
    balance += amount
    print("Deposit Successful")
    print("Updated Balance:", balance)
elif choice == 3:
    amount = float(input("Enter Withdraw Amount: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
elif choice == 4:
    print("Thank you for using our ATM.")
else:
    print("Invalid Choice")