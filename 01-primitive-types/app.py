
# Primitive data types
import math
student_count = 100  # number
rating = 4.9  # float
is_published = False  # Boolean
book_name = "Python"  # String
# print(student_count) # built in function


# String details
def _print(data, status=0):
    if (status == 1):
        print(data)


student_name = "Usman is here"  # double quotes are used to declare a string
student_goal = """
Goal is to complete the python in 15 days,
Moreover, 
tripple quotes
are used to write a string
in multiple lines
as i am writing
"""

_print(len(student_name))  # used to get the length of a string
_print(student_name[0])  # getting first character at index 0
_print(student_name[-1])  # getting last character at last index
# getting first three character from index 0 to 2
_print(student_name[0:3])
# getting first three character from index 0 to 2, if start index is not mentioned, it'll be zero by default
_print(student_name[:3])
# getting complete string, if second index is not add, it'll be the total length of string by default
_print(student_name[0:])
# getting complete string, if second index is not add, it'll be the total length of string by default
_print(student_name[0:len(student_name)])
# getting complete string, copy of original string
_print(student_name[:])
# Above 3 lines are returning same output


# --------------------------------------Escape Sequence ---------------------------------------

# we can't add " inside the string directly, for this we need to change the external quote from " to '
course = "   python programming   "
# to solve this there is a back slash
_print(course)
# other escape sequences
# \"
# \'
# \\
# \n , it'll split the string to new line


# --------------------------------------Formatted String ---------------------------------------


first = "Usman"
last = "Bakhsh"
full_name = first + " " + last
_print(full_name)
# New approach to concate the string, we can write any valid expressions in between curly braces
full_name = f"{first} {last}"
_print(full_name)


# -------------------------------------- String Methods ---------------------------------------

_print(course.capitalize())  # Converting to Capitalize
_print(course.upper())  # Converting to uppercase
_print(course.lower())  # Converting to lower case
_print(course.strip())  # trimming the string
_print(course.lstrip())  # trimming the string from left
_print(course.rstrip())  # trimming the string from right
_print(course.find("pro"))  # returning the index of pro in given string
# returning the index of x in given string, returning -1 in case of not existance
_print(course.find("x"))
_print(course.replace("p", "j"))  # replacing all p's to j's
_print("pro" in course)  # returning Boolean if string found
_print("swift" not in course)  # returning Boolean if string found
# returning count of character that is present in the string
_print(course.count("p"))
# converting a string into List, by default splitting from spaces
_print(course.split())


# -------------------------------------- Numbers ---------------------------------------
# there are three types of numbers
int_number = 10
float_num = 2.2
complex_num = 2 + 1j  # a + bi

_print(int_number + 3)  # addition
_print(int_number - 3)  # subtraction
_print(int_number * 3)  # multiplication
_print(int_number / 3)  # division, give floating point
_print(int_number // 3)  # give integer answer
_print(int_number % 3)  # Modulus, give remainder of divisions
_print(int_number ** 3)  # power


# Augmented assignment operator exists for all of the above
# x = 10
# x += 1
# x *= 2
# x /= 2
# x -= 2
# x %= 3
# x **= 3

# _print(x, 1)


# -------------------------------------- Built in functions for Numbers ---------------------------------------
_print(round(2.9))  # round off
_print(abs(-2.9))  # Absolute value
_print(math.ceil(2.9))  # return 3
_print(math.floor(2.9))  # return 2
_print(math.factorial(5))  # calculate factorial
_print(math.isqrt(121))  # find closest square root
_print(math.prod([1, 2, 3, 4, 5]))  # find the product of iteratable


# -------------------------------------- Type conversion  ---------------------------------------

# x = input("x: ")
# _print(type(x), 1) # type of input is str
# y = int(x) + 1
# _print(y, 1)

# other functions are
# int()
# bool()
# float()
# str()
