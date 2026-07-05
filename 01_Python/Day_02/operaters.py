# Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators")
print(a+b)  #Addition
print(a-b)  #Subtraction
print(a*b)  #Multiplication
print(a/b)  #Devide
print(a%b)  #Modulus(Remainder)
print(a**b) #Power
print(a//b) #Floor Division (Get the nearest value in int)
print("__________________________")

# Assignment Operators
print("Assignment Operators")
x = 10

x += 5      #(x=x+5)
print(x)

x -= 3      #(x=x-3)
print(x)

x *= 2      #(x=x*2)
print(x)

x /= 4      #(x=x/4)
print(x)
print("__________________________")

# Comparison Operators
a = 10
b = 20

print("Comparison Operators")
print(a == b)   #Equal  
print(a != b)   #Not Equal
print(a > b)    #Greater
print(a < b)    #Less
print(a >= b)   #Greater than Equal
print(a <= b)   #Less than Equal


# Logical Operators
# 1.AND
age = 20
print(age > 18 and age < 30)

# 2.OR
marks = 85
print(marks > 90 or marks > 80)

# 3.NOT
print(not True)   #It convert into opposite
print(not False)
print("__________________________")

# Identity Operators
# used to check whether two variables or objects point to the exact same memory location
a = 10
b = 10
print(a is b)
print(a is not b)

# Membership Operators
# used to test whether a value or variable exists within a sequence or iterable collection, such as a string, list, tuple, set, or dictionary
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)

