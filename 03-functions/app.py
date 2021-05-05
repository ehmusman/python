def _print(data, status=0):
    if (status == 1):
        print(data)
# ------------------------------ Functions -----------------------------


def greet(first_name, last_name):
    _print(f"Welcom {first_name} {last_name}")


def get_greet(first_name, last_name):
    return f"Welcom {first_name} {last_name}"

# greet("Usman", "Bakhsh")


# ------------------------------ Types of Functions -----------------------------
# 1- perform a task
# 2- return a value, it creates more reusability
message = get_greet("Usman", "Bakhsh")
# file = open("greet.txt", "w")
# file.write(message)
_print(greet("Usman", "Bakhsh"))
#  above will also return a None, that's an object that represent that nothing exists. by default each function returns a None

# ------------------------------ Keyword argument -----------------------------
#  this is used to add the parameter name in function argument while calling function


def increment(number, by):
    return number + by


_print(increment(2, by=1))

# ------------------------------ Default arguments -----------------------------
# to make the argument optional, we need to assign it a value right defining the function parameter


def increment_optional(number, by=1):
    return number + by


_print(increment_optional(2))

# ------------------------------ xargs -----------------------------
# for adding multiple arguments dynamically


def multiply(*numbers):
    # here these numbers are tuples, we can't change it but we can iterate it
    result = 1
    for number in numbers:
        result *= number
    return result


_print(multiply(1, 2, 3, 4))

# ------------------------------ xxargs -----------------------------


def save_user(**user):
    # **user, it'll return a dictionary, another data structure, just like objects
    _print(user["id"])
    _print(user["name"])
    _print(user["age"])


save_user(id=1, name="usman", age=29)


# ------------------------------ Scope -----------------------------

# variable defined inside a function has a functional scope, that variable can't be accessed from outside

# if same variable is defined globally, and we change it from the functiona scope variable having same name, the global variable will not be changed

# to change the global variable from function scope, we need to use the global variable

num = 10


def print_number():
    # global num # we should avoid to do this
    num = 5

print_number()
_print(num, 1)


# ------------------------------ FizzBuzz problem -----------------------------


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

_print(fizz_buzz(11), 1)