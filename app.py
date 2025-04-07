from collections import deque
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

# Scope
message = "a"


def greet(name):
    message = "b"


greet("Tahereh")
# These 2 messages are different. First one is global, and second one is local.
print(message)

# Fizzbuzz Function
# 1 - divisible by 3 -> fizz
# 2 - divisible by 5 -> buzz
# 3 - divisible by 3 and 5 -> fizzbuzz
# 4 - not divisible by 3 or 5 -> return just number


def fizz_buzz(input):
    divided_to_three = input % 3 == 0
    divided_by_five = input % 5 == 0
    if divided_to_three and divided_by_five:
        return "fizzBuzz"
    if divided_to_three:
        return "fizz"
    if divided_by_five:
        return "buzz"
    return input


print(fizz_buzz(45))

# Data structures
# Lists
numbers = list(range(20))
print(numbers[::2])  # Print even numbers
print(numbers[::-1])  # Print reversed list

numbers1 = [1, 2, 3]
# Unpacking list - the numbers of items in the list should be equal to the items unpacked
frist, second, third = numbers1
print(frist, second, third)

numbers2 = [1, 2, 3, 4, 4, 4, 4, 4]
# Packing list - Use *other for the rest of items
# Python with using * packes all the elements
first1, second1, *other = numbers2

print(first1, other)

# enumerate - The enumerate() function returns an enumerate object, which is an iterator.
# To see the pairs, you can convert it into a list or tuple:
fruits = ['apple', 'bannana', 'peach']
# print(list(enumerate(fruits)))

# Add or Remove data from list
# Add item to the end of the list
letters = ['a', 'b', 'c']
letters.append('d')
# Add in specific position
letters.insert(0, '-')
# Remove
# Remove item from the end of the list
# letters.pop()
# If you pass the index, that index will remove
letters.pop(1)
# First accurate "b" will remove.
# letters.remove("b")
# Remove a range of data
del letters[0:2]
# Clean the whole list
letters.clear()
# print('letters', letters)

# Fining items
chars = ["a", "b", "c", "d"]
print(chars.index("b"))
# If there is no 'd' in chars, this expression will return error.
# print(chars.index('d'))
# To prevent the error let check the chars:
if 'd' in chars:
    print(chars.index("d"))
# Count of an item => if > 0 there is atleast 1 item in list
print(letters.count("d"))

# Sortings stings and numbers
numberss = [3, 51, 4, 8, 23]
# Sort
# numberss.sort()
# It will reverse list and modified the original list
# numberss.sort(reverse=True)
# There is a built in function -> sorted()
# It would never change the list
print(sorted(numberss, reverse=True))
print(numberss)
# Sorting list of complex objects
# Ex: List of tuples -> Python doesnt know about sorting tuples
tupleItems = [
    ("Pro1", 10),
    ("Pro2", 9),
    ("Pro3", 12)
]
# def sort_item(item):
#     return item[1]
# tupleItems.sort(key=sort_item)

# using lambda fn instead of define "sort_item" (anonymous function)
tupleItems.sort(key=lambda item: item[1])
print(tupleItems)

# Map function -> 2 arguments -> lambda func and iterables -> It returns a map object
prices = list(map(lambda item: item[1], tupleItems))
# print('maped prices:', prices)

# Filter function -> 2 rguments -> func and iterables -> It returns a filter object
filtered = list(filter(lambda item: item[1] >= 10, tupleItems))
# print('filtered prices', filtered)

# List Comprehension -> [expression for item in items]
# Replace line 319
prices = [item[1] for item in tupleItems]
print('maped prices:', prices)
# Replace line 323
filtered = [item for item in tupleItems if item[1] >= 10]
print('filtered prices', filtered)

# Zip function -> multiple arguments -> if it has 2 arguments It creates a list of tuples, where each tuple has one element from each iterable.
# We wanna combine these two list
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))

# Stacks: LIFO behavior -> example: browser history
browsing_session = []
# next page
browsing_session.append(1)
# back to previus page
browsing_session.pop()
# We use inex negative to get item on top of the stack
# browsing_session[-1]
if not browsing_session:
    print("disbale")

# Queues: FIFO
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
# this function is not in lists
queue.popleft()
print(queue)
if not queue:
    print("Empty")

# Tuples
# creating tuples:
# point = (1, 2)
# point = 1,2
# point = 1,
# point = () -> empty tuple
# Concat 2 tuples:
# point = (1, 2) + (2, 3) -> (1,2,2,3)
# Repeat the tuple:
# point = (1, 2) * 3 -> (1,2,1,2,1,2)
# Convert a list to tuple -> using tuple fn:
# point = tuple([1,2]) -> (1,2)
# point = tuple("Hello") -> ("H", "e", "l", "l", "o")
# Get index of item or range of items:
# point = (1, 2, 3)
# print(point[0:2])
# x, y, x = point
# if 10 in point:
#     print("exists")
