# Conditional Statements (if)
# if (condition):
#      code

#1. The if Statement
age=20
if(age>=18):
    print("You are eligible for vote")
    
    
#2. The if-else Statement
marks = 30

if marks >= 35:
    print("Pass")
else:
    print("Fail")
    
#3. The if-elif-else Statement(Use this when you have multiple conditions.)
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
    
#4. Nested if
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Not Eligible")

    
