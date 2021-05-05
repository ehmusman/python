# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     factor = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didn't enter a valid age")
#     print(ex)
# # above clause is combining the below two clauses with different error exceptions
# # except ValueError as ex:
# #     print("You didn't enter a valid age", ValueError)
# #     print(ex)
# #     print(type(ex))
# # except ZeroDivisionError as ex:
# #     print("You didn't enter a valid age", ex)
# else:
#     print("No exceptions were thrown")
# finally: # Used to release the external resources. this will run every time. we can use this clause for cleaning purpose. like closing an opened file or un subscribing from an event that is subscribed before like remove socket connection listening/
#     print("Finally")
#     file.close()
# print("Execution Continues")

# ------------------------------ With Statement ------------------------
# it's used to replace the finally clause. it'll close the file automatically by calling the exit magic method
# try:
#     with open("app.py") as file:
#         print("File Open.", file.buffer)
#         # Magic Methods, used for context management protocol
#         # file.__enter__
#         # file.__exit__
#     age = int(input("Age: "))
#     factor = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didn't enter a valid age")
#     print(ex)
# else:
#     print("No exceptions were thrown")
# print("Execution Continues")


# ------------------------------ Rising Exceptions ------------------------

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age can't be 0 or less")
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as ex:
#     print(ex)


# ------------------------------ Cost of Rising Exceptions ------------------------
from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be 0 or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as ex:
    pass
    # print(ex)
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        None
    return 10 / age


factor = calculate_xfactor(-1)
if factor == None:
    pass
"""

# code2 is 4 times faster than code1. so before raising exceptions, we need to think twice
print("first code:", timeit(code2, number=10000))