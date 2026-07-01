# =========================================================
# Assignment-1: Python Basics & Variables
# =========================================================


# =========================================================
# 1. Print Your Name
# =========================================================

print("1. Print Your Name")
print("My name is Sagar Preetham Naidu")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Comments in Python
# =========================================================

print("2. Comments in Python")

# This is a single-line comment

print("This is single line comment")

print("""
This is a multi-line comment
Python uses triple quotes for multi-line comments or documentation
""")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Working with Basic Data Types
# =========================================================

print("3. Working with Basic Data Types")

integer_value = 100
float_value = 10.5
boolean_value = True
string_value = "Python"

print("Integer Value:", integer_value, "Type:", type(integer_value))
print("Float Value:", float_value, "Type:", type(float_value))
print("Boolean Value:", boolean_value, "Type:", type(boolean_value))
print("String Value:", string_value, "Type:", type(string_value))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Local vs Global Variables
# =========================================================

print("4. Local vs Global Variables")

value = "Global Variable"

def show_variables():
    
    value = "Local Variable"

    print("Inside function (Local):", value)
    print("Inside function (Global):", globals()["value"])


show_variables()

print("Outside function (Global):", value)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Type Checking & Dynamic Typing
# =========================================================

print("5. Type Checking & Dynamic Typing")

dynamic_variable = 100
print(dynamic_variable, "Type:", type(dynamic_variable))

dynamic_variable = 10.5
print(dynamic_variable, "Type:", type(dynamic_variable))

dynamic_variable = "Python"
print(dynamic_variable, "Type:", type(dynamic_variable))

dynamic_variable = True
print(dynamic_variable, "Type:", type(dynamic_variable))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. User Input Practice
# =========================================================

print("6. User Input Practice")

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name:", name)
print("Age:", age)

print("\n" + "=" * 50 + "\n")

