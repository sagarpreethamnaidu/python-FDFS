# =========================================================
# Assignment-2: Operators in Python
# =========================================================


# =========================================================
# 1. Basic Arithmetic Operations
# =========================================================

print("1. Basic Arithmetic Operations")


def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
   
arithmetic_operations(20, 2)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Simulating Increment and Decrement
# =========================================================

print("2. Simulating Increment and Decrement")


def increment_decrement(number):
    print("Number:", number)

    number += 1
    print("After Increment:", number)

    number -= 1
    print("After Decrement:", number)


increment_decrement(100)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Check if Two Numbers are Equal
# =========================================================

print("3. Check if Two Numbers are Equal")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("The numbers are not equal")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Relational Operators Demonstration
# =========================================================

print("4. Relational Operators Demonstration")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a < b :", a < b)
print("a <= b :", a <= b)
print("a > b :", a > b)
print("a >= b :", a >= b)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Find Smaller and Larger Numbers
# =========================================================

print("5. Find Smaller and Larger Numbers")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Larger Number:", num1)
    print("Smaller Number:", num2)
elif num2 > num1:
    print("Larger Number:", num2)
    print("Smaller Number:", num1)
else:
    print("Both numbers are equal")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Combine Conditions
# =========================================================

print("6. Find Largest Among Three Numbers")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. Operator-Based Calculator
# =========================================================

print("7. Operator-Based Calculator")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", number1 + number2)

elif operator == "-":
    print("Result:", number1 - number2)

elif operator == "*":
    print("Result:", number1 * number2)

elif operator == "/":
    if number2 != 0:
        print("Result:", number1 / number2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator entered")

print("\n" + "=" * 50 + "\n")
