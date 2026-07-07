# 📘 Python Day 4 Notes

## Name: Sahil Shantaram Tarle
## Topic: Loops (for Loop & while Loop)
## Day: 04

---

# 1. What is a Loop?

A loop is a programming concept that allows us to execute a block of code repeatedly until a condition becomes False.

Instead of writing the same code multiple times, we use loops.

### Example

Without Loop

```python
print("Hello")
print("Hello")
print("Hello")
```

With Loop

```python
for i in range(3):
    print("Hello")
```

---

# 2. Why Do We Use Loops?

Loops help us:

- Reduce code repetition
- Save time
- Make programs shorter
- Automate repetitive tasks
- Improve code readability

---

# 3. Types of Loops in Python

Python mainly provides two loops:

1. for Loop
2. while Loop

---

# 4. for Loop

A **for loop** is used when the number of iterations is known.

### Syntax

```python
for variable in range():
    statement
```

### Example

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# 5. range() Function

The `range()` function generates a sequence of numbers.

### Syntax

```python
range(stop)
```

Example

```python
range(5)
```

Output

```
0 1 2 3 4
```

---

### range(start, stop)

Example

```python
for i in range(1,6):
    print(i)
```

Output

```
1
2
3
4
5
```

---

### range(start, stop, step)

Example

```python
for i in range(2,11,2):
    print(i)
```

Output

```
2
4
6
8
10
```

---

# 6. while Loop

A **while loop** executes as long as the condition is True.

### Syntax

```python
while condition:
    statement
```

Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output

```
1
2
3
4
5
```

---

# 7. Difference Between for and while

| for Loop | while Loop |
|----------|------------|
| Used when iterations are known | Used when iterations are unknown |
| Uses range() | Uses a condition |
| Easier for counting | Better for user-controlled loops |

---

# 8. Loop Control Statements

## break

Stops the loop immediately.

Example

```python
for i in range(1,6):

    if i == 3:
        break

    print(i)
```

Output

```
1
2
```

---

## continue

Skips the current iteration.

Example

```python
for i in range(1,6):

    if i == 3:
        continue

    print(i)
```

Output

```
1
2
4
5
```

---

## pass

The `pass` statement does nothing.

It is used as a placeholder.

Example

```python
for i in range(5):
    pass

print("Finished")
```

---

# 9. Nested Loop

A Nested Loop means a loop inside another loop.

Example

```python
for i in range(3):

    for j in range(3):

        print(i, j)
```

Output

```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

# 10. Pattern Printing

Example

```python
for i in range(5):
    print("*")
```

Output

```
*
*
*
*
*
```

Triangle Pattern

```python
for i in range(1,6):
    print("*" * i)
```

Output

```
*
**
***
****
*****
```

---

# 11. Real-Life Applications of Loops

- ATM Machine Menu
- Login System
- Student Attendance
- Printing Reports
- Processing Data
- Games
- Data Analysis
- Machine Learning

---

# 12. Sample Programs

### Print Numbers 1 to 10

```python
for i in range(1,11):
    print(i)
```

---

### Print Even Numbers

```python
for i in range(2,21,2):
    print(i)
```

---

### Multiplication Table

```python
number = int(input("Enter Number: "))

for i in range(1,11):
    print(number, "x", i, "=", number * i)
```

---

### Factorial

```python
number = int(input("Enter Number: "))

fact = 1

for i in range(1, number + 1):
    fact *= i

print(fact)
```

---

# 13. Keywords Learned Today

- for
- while
- range()
- break
- continue
- pass
- Nested Loop

---

# 14. Interview Questions

### Q1. What is a loop?

**Answer:**
A loop is used to execute a block of code repeatedly until a condition becomes False.

---

### Q2. What are the types of loops in Python?

**Answer:**

- for loop
- while loop

---

### Q3. When should we use a for loop?

**Answer:**
Use a for loop when the number of iterations is known.

---

### Q4. When should we use a while loop?

**Answer:**
Use a while loop when the number of iterations is unknown and depends on a condition.

---

### Q5. What is the use of range()?

**Answer:**
The range() function generates a sequence of numbers.

---

### Q6. What is break?

**Answer:**
break immediately terminates the loop.

---

### Q7. What is continue?

**Answer:**
continue skips the current iteration and moves to the next iteration.

---

### Q8. What is pass?

**Answer:**
pass is a placeholder statement that performs no action.

---

### Q9. What is a Nested Loop?

**Answer:**
A Nested Loop is a loop inside another loop.

---

### Q10. Give two real-life examples of loops.

**Answer:**

- ATM Machine Menu
- Student Attendance System

---

# 15. Summary

Today I learned about loops in Python. I learned how to use for loops, while loops, range(), break, continue, pass, nested loops, and pattern printing. Loops help us write shorter and more efficient programs by avoiding repetitive code.

---

# 🎯 Key Points to Remember

- Loops reduce repetitive code.
- Python has two main loops: for and while.
- range() is mainly used with for loops.
- break stops the loop.
- continue skips one iteration.
- pass is a placeholder.
- Nested loops are used for patterns and complex logic.

---

# 📌 Common Mistakes

❌ Forgetting indentation

```python
for i in range(5):
print(i)
```

✅ Correct

```python
for i in range(5):
    print(i)
```

---

❌ Infinite while loop

```python
i = 1

while i <= 5:
    print(i)
```

✅ Correct

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# 🚀 Revision Points

✅ What is a loop?

✅ Types of loops

✅ range()

✅ for loop

✅ while loop

✅ break

✅ continue

✅ pass

✅ Nested loop

✅ Pattern printing

---
