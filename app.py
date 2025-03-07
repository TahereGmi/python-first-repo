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

# x = input("x: ")
# # y = x + 1
# # These 2 have different types and this expression have syntax error.
# print(type(x))  # This expression shows type string for x
# y = int(x) + 1  # Should convert x to int and return it as a int value.
# print(f"x: {x}, Y: {y}")

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

# Iterables
# for x in range(4) => range is iterable (Tekrar pazir)
# for x in "Python" => strings could be iterable
# for x in [1,2,3] => lists could be iterable

# While loops
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("Echo", command)

counter = 0
# number = 0
# while number < 10:
#     number += 2
#     counter += 1
#     print(number)
#     if number == 8:
#         print(f"We have {counter} even numbers!")
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        counter += 1
print(f"We have {counter} even numbers!")

# Functions


def greeting(first_name, last_name):
    print("My first function")
    print(f"{first_name} {last_name}")


greeting("Tahereh", "Gholami")

# 2 types of function:
# 1- Perform a task
# 2- Return a value

# Keyword argument: when our function have multiple arguments use if for make more clear
# example:


def increment(number, by):
    return number + by


print(increment(2, by=3))  # using keyword argument
# Default argument
# If you dont add second argument, the function has default argument


def increment_by_default(number, by=2):
    return number + by


print(increment_by_default(2))
# Point: All the optional parameters should come after required parameters

# xargs => *numbers => data structure in python: tuple


# => this structure (*numbers) is tuple. you can iterate on it.
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# xxargs => **users => data structure in puthon is dictionary

# => this structure (*numbers) is dictionary. you can access to items by its key.


def save_user(**user):
    print(user)
    print(user["id"])


save_user(id=1, name="Tahereh", job="developer")
