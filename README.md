# Python Basics 📘

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
name = "Debadyuti"   # string
is_valid = True # boolean

numbers = [1,2,3]   # list
point = (1,2)       # tuple
unique = {1,2,3}    # set
student = {"name":"Parthib", "age":20}  # dict
```

### Complex Data Type (complex)

#### 🔹 Short Theory

Complex numbers are used to represent numbers with a real and imaginary part.
Format: `a + bj` where `j` is the imaginary unit.

#### Example Code

```python
z = 2 + 3j
print(z.real)  # 2.0
print(z.imag)  # 3.0
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
name = "Rajdeep"
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

## 4. User Input & Type Casting

### 🔹 Short Theory

Python allows taking input from users using the `input()` function. By default, input is always stored as a string, so type casting is used to convert it into the required data type.

### Example Code

```python
# Taking input
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name)
print("Your age is", age)
```

### Type Casting

```python
# Converting input types
age = int(input("Enter your age: "))
price = float(input("Enter price: "))

print(age + 5)       # works as integer
print(price + 10.5)  # works as float
```

### Common Type Casting Functions

* int()   → converts to integer
* float() → converts to float
* str()   → converts to string
* bool()  → converts to boolean

---

## Summary

* Python is dynamically typed
* Data types define the kind of value
* Variables store data
* Conditionals control program flow

---

Happy Coding 🚀
