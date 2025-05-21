from sys import getsizeof
from array import array
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

# Swapping variables:
x = 10
y = 11
# ** just one line:
x, y = y, x
# On the right side its a tuple. It exact equals to:
# x, y = (11, 10)  -> x, y extract from this tuple

# Array -> If you are dealing with a large secuense number use arrays So dont solve the problem that doesnt exist.
# array(typecode, ...) -> you have to set the typecode -> google it
numbers = array("i", [1, 2, 3])
# This line cause an error because this array onle must have integer -> typecode
# numbers[0] = 1.0

# Sets
# Make lists items unique
# **** rnumbers = [1, 1, 2, 3, 4]
# uniques = set(rnumbers)
# print("uniques:", uniques)
# print("unique len:", len(uniques))
# **** first = set(numbers)
# **** second = {1, 5}
# print(first | second) -> both sets items: {1,2,3,4,5}
# print(first & second) -> just common items: {1}
# print(first - second) -> {2,3,4}
# print(first ^ seconf) -> items are either in the first or second sets but not both: {2,3,4,5}
# Sets unlike lists are unordered collection. It means sets are not in sequence so we can not access them using an index.
# print(first[0]) -> error
# If you wan to access items with index you must use list, or:
# if 1 in first:
#     print("Yes")

# Dictionaries data structure
# Python doesn’t have “objects” in the same sense as JavaScript
# It just has dictionaries for key-value storage (and classes for OOP-style objects).
# - Built-in key-value storage.
# - Keys must be hashable (strings, numbers, tuples, etc).
point = dict(x=1, y=2)  # -> {"x":1, "y":2}
print(point["x"])
point["z"] = 20
print(point.get("a", 0))  # if "a" exist it returns and if not returns 0
del point["x"]
# for key in point:
#     print(key, point[key])
for key, value in point.items():
    print(key, value)


# Dictionary comprehensions
# {expression for item in items}
# values = {x*2 for x in range(5)}  ->  this returns a set expression
# values = {x: x*2 for x in range(5)}  -> this returns a dictionary expression
# values = (x*2 for x in range(5)) -> this returns a generator expression
# print(values)

# Generator expressions -> constant size for how many size data
values = (x*2 for x in range(10))
print("gen:", getsizeof(values))


# Unpacking operator
snumber = [1, 2, 3]
print(*snumber)  # using * unpacking the list
values = [*range(5), *"Hello"]
print("unpacked values:", values)
first = [1, 2]
second = [3]
combined = [*first, "a", *second]
print("combined values:", combined)
# Unpack dictionary
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second}
# Using 2 stars (**) to unpacking as a key: value. with just one star (*) it will return just keys.
# Also if there is repeated items in dictionaries, last value will use.
print("combined dictionaries:", combined)

# Exceptions: error msgs or exceptions that terminate the code
# How to handle it: ValueError helps to not terminate the code
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    # Actual error
    print(ex)
    print(type(ex))
# When no exception
else:
    print("No exceptions were thrown.")

# There would be different exceptions with same msg,
# we can write them like this -> except (ValueError, ZeroDivisionError):

# there are times we need to work with external resources like files, newtwork connections, data bases, ...
# whenever we use these resources, after we have done, we need to relase that.
# For example: when we open the file, we should close it after we have done.
# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactore = 10 / age
    # If above line throws an exception this line never execute
    # file.close()
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# # Always executed
# finally:
#     file.close()

# Built-in exceptions -> you can google it
# Raising exceptions


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


# At this line programe will crash
# calculate_xfactor(-1)
# Implement in try and add except, it will not crash
# Raising exception has cost, if you are budingl large scale apps, be careful to use it.
# if you can handle situations with simple if statements, do it
try:
    calculate_xfactor(-1)
except ValueError as err:
    print(err)

# ******* Classes ******
# Class: blueprint for creating new objects (related data and objects)
# Object: instance of a class
# Class: Human
# Objects: John, Mary, Jack

# Custom classes


class Point:
    defaul_color = "red"
    # Contrsutor

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Draw point ({self.x}, {self.y})")


# point = Point(1, 2)
# print(isinstance(point, Point))  # -> True
# point.draw()
# Class attributes shared across all the instanses.
# print(Point.defaul_color)
# print(point.defaul_color)
# If you change the class attribute, the change is visible in all the instances
# Point.defaul_color = "yellow"
# print(point.defaul_color) -> yellow

# ****** class vs instance method *******
# @classmethod is a tool.
# - A method that belongs to the class, not the instance.
# - First parameter is cls, not self.
# - You can use it to create alternative constructors.
# >>>>>> Factory method -> This pattern is common when:
# - A design pattern used to encapsulate object creation logic
# - Often returns instances of subclasses or configures the object.
# - In Python, it’s commonly implemented as a @classmethod.
# - You want to access or modify class-level state,
# - Without needing to create an object.

# A factory method is a special kind of classmethod,
# but a classmethod could just be any method tied to the class instead of an instance —
# it might return a number, config, or log something.
# It's not a factory unless it's creating instances

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)  # -> equal to Point(0,0) -> Factory method

    # instance method
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()  # -> Factory method
point.draw()

# Magic methods:
# also called dunder methods for “double underscore”) are special methods that start and end with two underscores like:
# __init__, __str__, __len__, __add__, __eq__, etc.
# They’re used to customize how your objects behave — for example, when you print them, compare them, or use built-in functions on them.
# Python automatically calls these methods behind the scenes when certain operations happen.
# You don't call them directly — Python does it for you.
# To see all the magic methods, google it.

# Comparing 2 objects:


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # If we dont have this method, by default this equality operator (==) compares addresss or references of these 2 object in memory.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point1(2, 4)
other = Point1(1, 2)
# print(point == other)
# print(point > other)

# Performing arithmetic operations:


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(p1, p2):
        return Point2(p1.x + p2.x, p1.y + p2.y)


p1 = Point2(10, 11)
p2 = Point2(2, 3)
combined = p1 + p2
# print(combined.x) # ->12

# ********* Making custom containers **********
# While Python’s built-in containers (list, dict, set, etc.)
# cover most common use cases, sometimes you’ll need custom containers when:
# 1.You want to enforce specific behavior or rules:
# - A list that only allows integers.
# - A dictionary that automatically converts all keys to lowercase.
# 2.You want to add extra features or logic:
# - Logging when items are added/removed.
# - Automatically saving to a file when updated.
# - Lazy loading data on access.
# 3.You want to mimic or extend built-in types
# - Acts like a list, but is backed by a database.
# - Feels like a dictionary, but fetches keys from an API.
# 4.For clean code and reuse in large projects
# If you have a common pattern—like a list that tracks history
# or a set with expiration—you can put it in a custom container and reuse it.


class TagClouds:
    def __init__(self):
        self.tags = {}
        # Private member
        self.__counts = []

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagClouds()
# getItem, setItem
cloud["Python"] = 10
# add
cloud.add("Python")
cloud.add("python")
# len
len(cloud)

# **** When you define something with two leading underscores,
# like __count, Python will "mangle" the name to prevent accidental access *****

# ****** Private Members ******
# We can make certian attributes or certain classess private, If we prefix them with __, they are considered private.
# How you can access them?
# __dict__ -> holds all the attributes on this class
print(cloud.__dict__)
# You can access this private memmber:
print(cloud._TagClouds__counts)

# ******** Properties *********
# A property lets you use a method like a variable.

# So instead of calling a method like this:
# person.get_name() -> person.name
# But behind the scenes, it’s still calling a method! 
# This is useful when you want to run some code when ** getting or setting ** a value, like checking if the value is valid.

# Basic example
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # This runs when you do person.name
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):  # This runs when you do person.name = "New Name"
        print("Setting name...")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

# usage
p = Person("Alice")

print(p.name)      # ➜ Getting name... ➜ Alice

p.name = "Bob"     # ➜ Setting name...

# p.name = 123       # Error: Name must be a string

# Why use it?
# You want to protect your data (e.g., check it before saving)
# You want to compute a value instead of storing it
# You want to hide internal logic
# Remember:
# @property → makes a method act like a variable
# @name.setter → runs when you change the value
# @name.deleter (optional) → runs when you delete it


# ************ Inheritance
class Animal():
    def __init__(self):
        self.age = 1
        print("Animal contructor!")
    def eat(self):
        print("Eat")

# Animal: Parent, Base
# Mammal: Child, sub
class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        super().__init__() # --> add Animal class contructor to this class
    def walk(self):
        print("Walk")
    
class Fish(Animal):
    def swim(self):
        print("Swim")
m = Mammal()
m.eat() # -> Inherited from Animal class

# print(isinstance(m, Animal)) #-> True
# ** There is a base class (built in class) for all the classes in python -> object class
# print(isinstance(m, object)) #-> True
# o = object() #-> An empty object
# ** There is another built in class -> issubclass
# print(issubclass(Mammal, Animal)) #-> True
# print(issubclass(Mammal, object)) #-> True

# ************* Method Overriding
# When a class inherit from other, the contructor of class replaces to base class one. -> line 742

# *** AVOID USING INHERITANCE MULTI-LEVEL, MORE THAN 1-2 LEVEL TO PREVENT MORE COMPLEXITY ****


# *********** Multiple Inheritence ***********
# There is no common mudule between classes
# If there is common mudoles it causes some problems
class Flyer():
    def fly(self):
        pass
class Swimmer():
    def swim(self):
        pass
class FishFlyer(Flyer, Swimmer):
    pass

# A good example and introducing abstract class:
from abc import ABC, abstractmethod
class InvalidOperationError(Exception):
    pass
class Stream(ABC):
    def __init__(self):
        self.opened = False
    
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("File Stream")

class NetworkStream(Stream):
    def read(self):
        print("Memory Stream")



