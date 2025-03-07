import math

print("Hello world!")
print("*"*10)
x = 1
# Primitive variables: string, number, boolean
course_count = 1000
x = 3.5
course_name = "  Python programming"
# print(course_name[0])
# print(course_name[:])
# print(course_name[-1:])
# print(len(course_name))

first = "Tahereh"
last = "Gholami"
full = f"{len(first)} {last}"
print(full)

# string methods
print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.strip())
print(course_name.lstrip())
print(course_name.find("ro"))
print(course_name.replace("p", "j"))
print("pro" in course_name)
print("test" not in course_name)

# Numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# Working with numbers
print(round(2.8))
print(abs(-2.4))
print(math.ceil(3.2))

# Type conversion

x = input("x: ")
# y = x + 1
# These 2 have different types and this expression have syntax error.
print(type(x))  # This expression shows type string for x
y = int(x) + 1  # Should convert x to int and return it as a int value.
print(f"x: {x}, Y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)
fruit = "Apple"
print(fruit[1:-1])


# Conditional statements
temperature = 35
if temperature > 30:
    print("It's Warm")
    print("Drint water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print('Done')

# Ternary Operator
age = 13
message = "Eligable" if age >= 18 else "Not eligable"
print(message)

# Logical Operators
# and, or, not
high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligable")
else:
    print("Not eligable")

# Short circuit evaluation
# If one of theme are False, python interperetor stop evaluation:
# *******if high_income and good_credit and not student
#  If one of them are True, python interpretor stop evaluation.
# It checks first vraible, if it's false then next, until finds True value, then stops evaluation
# ******* if high_income or good_credit or not student

# Chaining comparison oparators
# Expression: age should be between 18 and 65
age = 22
# if age >= 18 and age < 65: can write like bellow:
if 18 <= age < 65:
    print("Eligable")

# For loops
# from 1 to 10 with 2 step
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# For ... Else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed!")
