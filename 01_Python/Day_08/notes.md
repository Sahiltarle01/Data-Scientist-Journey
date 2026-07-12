# Python Day 8 Notes

# Name
Sahil Shantaram Tarle

# Topic
Dictionaries

# What is a Dictionary?

A dictionary is a collection of data stored in key-value pairs. It is mutable, ordered, and allows unique keys.

```python
# Creating a Dictionary
student = {
    "name": "Sahil",
    "age": 20,
    "branch": "AI & Data Science"
}

print(student)
```

# Why Do We Use Dictionaries?

Dictionaries are used to store related information together.

Example:

```python
# Student Information
student = {
    "name": "Sahil",
    "age": 20,
    "city": "Nashik"
}
```

# Dictionary Characteristics

- Stores data in key-value pairs.
- Mutable.
- Ordered.
- Keys must be unique.
- Values can be duplicated.

# Creating Dictionaries

```python
# Dictionary Example
employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 50000
}

print(employee)
```

# Access Dictionary Values

```python
# Access Using Key
student = {
    "name": "Sahil",
    "age": 20
}

print(student["name"])
print(student["age"])
```

# Access Using get()

```python
# get() Method
print(student.get("name"))
```

# Add New Item

```python
# Adding New Key-Value Pair
student["college"] = "Sanjivani University"

print(student)
```

# Update Existing Value

```python
# Updating Value
student["age"] = 21

print(student)
```

# Remove Item Using pop()

```python
# pop() Method
student.pop("age")

print(student)
```

# Remove Item Using del

```python
# del Keyword
del student["college"]

print(student)
```

# Clear Dictionary

```python
# clear() Method
student.clear()

print(student)
```

# Dictionary Methods

```python
# keys() Method
student = {
    "name": "Sahil",
    "age": 20,
    "city": "Nashik"
}

print(student.keys())
```

```python
# values() Method
print(student.values())
```

```python
# items() Method
print(student.items())
```

```python
# update() Method
student.update({"branch": "AI & Data Science"})

print(student)
```

# Loop Through Dictionary Keys

```python
# Print Keys
for key in student:
    print(key)
```

# Loop Through Dictionary Values

```python
# Print Values
for value in student.values():
    print(value)
```

# Loop Through Keys and Values

```python
# Print Keys and Values
for key, value in student.items():
    print(key, value)
```

# Membership Operator

```python
# Check Key Exists
print("name" in student)
print("phone" in student)
```

# Nested Dictionary

```python
# Nested Dictionary
students = {
    "student1": {
        "name": "Sahil",
        "marks": 90
    },
    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}

print(students["student1"]["name"])
print(students["student2"]["marks"])
```

# Dictionary Functions

```python
# Length of Dictionary
print(len(student))
```

# Difference Between List, Tuple, Set and Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---------|------|--------|-----|------------|
| Symbol | [] | () | {} | {} |
| Ordered | Yes | Yes | No | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicate Values | Yes | Yes | No | Values Only |
| Key-Value Pair | No | No | No | Yes |

# Real Life Applications

- Student Management System
- Employee Records
- Banking Applications
- APIs
- JSON Data
- Machine Learning
- Data Science
- Contact Management

# Interview Questions

1. What is a Dictionary?
2. Why do we use Dictionaries?
3. What is a Key?
4. What is a Value?
5. What is the difference between get() and []?
6. What is the difference between pop() and del?
7. What does keys() return?
8. What does values() return?
9. What does items() return?
10. What is a Nested Dictionary?

# Keywords

Dictionary

Key

Value

get()

keys()

values()

items()

update()

pop()

del

clear()

Nested Dictionary

Membership Operator

# Summary

Today I learned about Python Dictionaries. I learned how to create dictionaries, access values, add new key-value pairs, update existing values, remove items, use dictionary methods like keys(), values(), items(), update(), pop(), and clear(). I also learned how to loop through dictionaries and create nested dictionaries. Dictionaries are widely used in APIs, JSON files, Data Science, and Machine Learning.

# Key Points to Remember

- Dictionaries store data as key-value pairs.
- Keys must be unique.
- Values can be duplicated.
- Dictionaries are mutable.
- Access values using keys.
- get() safely accesses values.
- keys() returns all keys.
- values() returns all values.
- items() returns key-value pairs.
- update() updates or adds items.
- pop() removes an item by key.
- del removes a key-value pair.
- clear() removes all items.
- Nested dictionaries store dictionaries inside dictionaries.
