# =========================================================
# Assignment-3: Loops & Control Flow in Python
# =========================================================


# =========================================================
# 1. Print a Message Multiple Times
# =========================================================

print("1. Print a Message Multiple Times")

for i in range(10):
    print("Hello This is Sagar")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Print Numbers Using While Loop
# =========================================================

print("2. Print Numbers Using While Loop")

num = 1

while num <= 20:
    print(num)
    num += 1

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Equal and Not Equal Check
# =========================================================

print("3. Equal and Not Equal Check")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

if num1 != num2:
    print("The numbers are not equal.")
else:
    print("The numbers are equal.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Odd and Even Numbers
# =========================================================

print("4. Odd and Even Numbers from 1 to 50")

for num in range(1, 51):

    if num % 2 == 0:
        print(num, "- Even")
    else:
        print(num, "- Odd")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Largest Among Three Numbers
# =========================================================

print("5. Largest Among Three Numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Even Numbers in a Range
# =========================================================

print("6. Even Numbers Between 10 and 20")

i = 10

while i <= 20:

    if i % 2 == 0:
        print(i)

    i += 1

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. Armstrong Number
# =========================================================

print("7. Armstrong Number Check")

num = int(input("Enter a number: "))

digits = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 8. Prime Number Check
# =========================================================

print("8. Prime Number Check")

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 9. Palindrome Check
# =========================================================

print("9. Palindrome Check")

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 10. Even or Odd (Using Conditions)
# =========================================================

print("10. Even or Odd Check")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 11. Gender Identification
# =========================================================

print("11. Gender Identification")

gender = input("Enter Gender (M/F): ")

if gender == 'M' or gender == 'm':
    print("Male")
elif gender == 'F' or gender == 'f':
    print("Female")
else:
    print("Invalid Input")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 12. Multiplication Table Generator
# =========================================================

print("12. Multiplication Table Generator")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 13. Count Digits in a Number
# =========================================================

print("13. Count Digits in a Number")

num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        count += 1
        num //= 10

print("Number of digits:", count)

print("\n" + "=" * 50 + "\n")
