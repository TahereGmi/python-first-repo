# Find the most repeated character
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)
# we should sort char_frequency to find the most repeated character
# as we know dictionaries like sets are unordered collections, we can not sort them.
# so basicaly we need to take out each key: value pair, convert it to tuples and put it in a list to sort them.

# print(sorted(char_frequency.items()))
# char_frequency.items() -> this returns all key: value pairs as tuple
# sorted() -> returns a sorted list
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_frequency_sorted[0])

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
try:
    calculate_xfactor(-1)
except ValueError as err:
    print(err)
