# 📘 Python Day 2 Notes

## Name: Sahil Shantaram Tarle
## Topic: Operators & Type Casting
## Day: 02

---

# 1. What are Operators?

Operators are special symbols used to perform operations on variables and values.

### Example

```python
a = 10
b = 5

print(a + b)
```

Output:

```
15
```

---

# 2. Types of Operators in Python

Python has the following types of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators (Advanced)

---

# 3. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| // | Floor Division | 10 // 3 |
| % | Modulus (Remainder) | 10 % 3 |
| ** | Exponent (Power) | 2 ** 3 |

### Example

```python
a = 20
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)
```

---

# 4. Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example |
|----------|---------|
| = | x = 10 |
| += | x += 5 |
| -= | x -= 2 |
| *= | x *= 3 |
| /= | x /= 2 |
| %= | x %= 2 |

### Example

```python
x = 10

x += 5
print(x)

x -= 3
print(x)
```

---

# 5. Comparison Operators

Comparison operators compare two values and return **True** or **False**.

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

### Example

```python
a = 10
b = 20

print(a == b)
print(a < b)
print(a != b)
```

---

# 6. Logical Operators

Logical operators combine two or more conditions.

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the result |

### Example

```python
age = 20

print(age > 18 and age < 30)
print(age > 18 or age < 10)
print(not(age > 18))
```

---

# 7. Identity Operators

Identity operators compare the memory location of two objects.

| Operator | Meaning |
|----------|---------|
| is | Same object |
| is not | Different object |

### Example

```python
a = 10
b = 10

print(a is b)
print(a is not b)
```

---

# 8. Membership Operators

Membership operators check whether a value exists inside a sequence.

| Operator | Meaning |
|----------|---------|
| in | Exists |
| not in | Does not exist |

### Example

```python
languages = ["Python", "Java", "SQL"]

print("Python" in languages)
print("C++" in languages)
```

---

# 9. Type Casting

Type casting means converting one data type into another.

### Types of Type Casting

- int()
- float()
- str()
- bool()

### Example

```python
number = "100"

print(type(number))

number = int(number)

print(type(number))
```

---

# 10. Converting Data Types

### String to Integer

```python
num = int("50")
```

### Integer to Float

```python
num = float(50)
```

### Float to String

```python
num = str(10.5)
```

---

# 11. Difference Between '/' and '//'

| / | // |
|---|----|
| Returns decimal value | Returns whole number |

### Example

```python
print(10 / 3)
print(10 // 3)
```

Output

```
3.333333
3
```

---

# 12. Difference Between '=' and '=='

| = | == |
|---|----|
| Assignment Operator | Comparison Operator |

Example

```python
x = 10
print(x == 10)
```

---

# 13. Keywords Learned Today

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Type Casting
- int()
- float()
- str()

---

# 14. Interview Questions

### Q1. What is an operator?
**Answer:** An operator is a symbol that performs operations on values or variables.

### Q2. Name the arithmetic operators.
**Answer:** +, -, *, /, //, %, **

### Q3. What is the difference between '/' and '//'?
**Answer:** '/' returns decimal division, while '//' returns floor division.

### Q4. What is type casting?
**Answer:** Type casting is the process of converting one data type into another.

### Q5. Name three type casting functions.
**Answer:** int(), float(), str()

### Q6. What does '%' operator do?
**Answer:** It returns the remainder after division.

### Q7. What is the difference between '=' and '=='?
**Answer:** '=' assigns a value, while '==' compares two values.

### Q8. What is the output of:

```python
print(2 ** 3)
```

**Answer:** 8

---

# 15. Summary

Today I learned about Python operators and type casting. I learned arithmetic, assignment, comparison, logical, identity, and membership operators. I also learned how to convert one data type into another using int(), float(), and str(). These concepts are useful for writing programs and solving real-world problems.

---