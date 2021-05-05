# ---------------------------------- Comparison Operators  --------------------------------

# >, <, >=, <=, ==,

# ---------------------------------- Conditional Statements  --------------------------------

def _print(data, status=0):
    if (status == 1):
        print(data)


temperature = 12
if temperature > 30:
    _print("it's too hot")
    _print("Drink water")
elif temperature > 20:
    _print("it's normal temperature")
else:
    _print("it's cold")
_print("Done")

# ---------------------------------- Ternary operator  --------------------------------

age = 22
message = "Eligible" if age >= 18 else "Not eligible"
_print(message)


# ---------------------------------- Logical operators  --------------------------------

# and
# or
# not
high_incom = True
good_credit = True

if (high_incom and good_credit):
    _print("Eligible")
else:
    _print("Not eligible")

# ---------------------------------- Short circuit eveluation  --------------------------------

# in case of and operator, if first argument is False, the next expressions will not be evaluated because the combined result will be False, if First expressions will be True, the second will be checked and so on, if any one is False, the next will not be evaluated

# in case of or operator, if first expression is True, the next will not be evaluated and so on.


# ------------------------------ Chaining comparison operator -----------------------------

if 18 <= age < 65:  # this condition is looking like a normal math statement, it's also valid in python
    _print("Eligible")


# ------------------------------ For loop -----------------------------

for number in range(1, 4):
    _print(f"Attempt {number}")

# range(3) , it'll return 0,1,2
# range(1,4), it'll return 1,2,3 => it'll start from 1
# range(1,10,2), here it'll start from 1, with step 2 untill 1t reaches 10


# ------------------------------ For else loop -----------------------------
success = False
for number in range(1, 4):
    _print(f"Attempt {number}")
    if success:
        _print("Successful")
        break
else:  # if the loop has run successfully without break, this else will be executed
    _print("Attempted 3 timies")

# ------------------------------ Nested loops -----------------------------
#  Draw the x,y coordinated
for x in range(5):
    for y in range(3):
        _print(f"x:{x}, y:{y}")

# ------------------------------ Iterables -----------------------------
_print(type(5))
# loop run for the iterables only
_print(type(range(5)))
# range is iterable
# string is also iterable
# List is also iterables

for x in "python":
    _print(f"x:{x}")

for x in [1, 2, 3]:
    _print(x)


# ------------------------------ While loop -----------------------------
number = 100
while number > 0:
    _print(number, 1)
    number //= 2
