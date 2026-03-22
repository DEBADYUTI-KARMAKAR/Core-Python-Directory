# Python Core 📘

This README covers core Python fundamentals:

* Data Types
* Variables
* Conditionals

---

## 1. Data Types

### 🔹 Short Theory

Python has built-in data types used to store different kinds of values.

### Common Data Types

| Type  | Example    | Description                   |
| ----- | ---------- | ----------------------------- |
| int   | 10         | Integer numbers               |
| float | 10.5       | Decimal numbers               |
| str   | "hello"    | Text data                     |
| bool  | True/False | Boolean values                |
| list  | [1,2,3]    | Ordered, mutable collection   |
| tuple | (1,2,3)    | Ordered, immutable collection |
| set   | {1,2,3}    | Unordered, unique values      |
| dict  | {"a":1}    | Key-value pairs               |

### Example Code

```python
x = 10          # int
y = 10.5        # float
name = "John"   # string
is_valid = True # boolean

numbers = [1,2,3]   # list
point = (1,2)       # tuple
unique = {1,2,3}    # set
student = {"name":"John", "age":20}  # dict
```

---

## 2. Variables

### 🔹 Short Theory

Variables are used to store data. Python is dynamically typed, so you don’t need to declare the type.

### Rules

* Must start with a letter or underscore
* Cannot start with a number
* Case-sensitive (age ≠ Age)

### Example Code

```python
x = 5
name = "Alice"
price = 99.99

# Multiple assignment
a, b, c = 1, 2, 3

# Dynamic typing
x = 10
x = "Now I'm a string"
```

---

## 3. Conditionals

### 🔹 Short Theory

Conditionals are used to make decisions in code.

### Keywords

* if
* elif
* else

### Example Code

```python
age = 18

if age > 18:
    print("Adult")
elif age == 18:
    print("Just Adult")
else:
    print("Minor")
```

### Logical Operators

```python
x = 10

if x > 5 and x < 15:
    print("Between 5 and 15")

if x == 10 or x == 20:
    print("x is 10 or 20")

if not x == 0:
    print("x is not zero")
```

---


## Summary

* Python is dynamically typed
* Data types define the kind of value
* Variables store data
* Conditionals control program flow

---

Happy Coding 🚀
