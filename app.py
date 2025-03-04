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
