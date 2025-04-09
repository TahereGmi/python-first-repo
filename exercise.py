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
print("Execution continues.")
