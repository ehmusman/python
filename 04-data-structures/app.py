from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque


def _print(data, status=0):
    if (status == 1):
        print(data)


# ------------------------------ Lists -----------------------------
latters = ["a", "b", "c"]  # List of laters
numbers = [1, 2, 3, 4]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 10
combined = zeros + latters
_print(combined)  # list of 10 zeros

numbers = list(range(20))  # 20 is not included in the list
latters = list("Python Programming")  # 20 is not included in the list
_print(latters)
_print(len(latters))  # finding length of list


# ------------------------------ Accessing items -----------------------------
_print(latters[0])  # accessing first index
_print(latters[-1])  # accessing last index
_print(latters[3:])  # slicing the list from 3rd index to last index
_print(latters[:4])  # slicing the list from 0 index to 4rth element
_print(latters[:])  # clonning the existing list
# latters[0]="A" # Modifying the first element
_print(latters[::2])  # returning every second element of list
_print(latters[::3])  # returning every third element of list
_print(latters[::-1])  # returning reverse array

# ------------------------------ Unpacking Lists -----------------------------


numbers = [1, 2, 3]
first, second, third = numbers
# if the left side variables are not equal to length of list, it'll throw an error
_print(f"{first} {second} {third}")

# Packing and unpacking
first, second, *other = list(range(10))
first, *other, last = list(range(10))
_print(f"{first} {last} {other}")


# ------------------------------ Looping over Lists -----------------------------

for number in numbers:
    _print(number)

# to get the index also
for number in enumerate(numbers):
    # here number is a tupple
    _print(f"index: {number[0]} element: {number[1]}")

# to get the index also
for index, number in enumerate(numbers):
    _print(f"index: {index} element: {number}")


# ------------------------------ Adding or removing items in the list ------------------------
# Add
numbers.append(4)  # adding at the last of the list
_print(numbers)

numbers.insert(0, 0)  # adding at zero index
_print(numbers)

numbers.insert(3, 3)  # adding at third index
_print(numbers)

# Remove
lastElement = numbers.pop()
_print(numbers)  # it'll remove item from the end of the list

lastElement = numbers.pop(0)
_print(numbers)  # it'll remove item from the start of the list

lastElement = numbers.pop(1)
_print(numbers)  # it'll remove item from the second index of the list

numbers.remove(3)  # it'll remove the first occurance of 3 in the list
_print(numbers)

# it'll remove the 1 item from index 0, we can delete a range of items
del numbers[0:1]
_print(numbers)

numbers.clear()  # it'll remove all the items
_print(numbers)


# ------------------------------ Finding items in the list ------------------------
letters = ["a", "b", "c"]
_print(letters.index("b"))  # it'll return the index of b element
# if element is not present in the list, it throws an error
if "d" in latters:
    _print(letters.index("d"))  # it'll return the index of b element

_print(letters.count("b"))  # it'll return the index of b element


# ------------------------------ Sorting items in the list ------------------------
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
_print(numbers)
numbers.sort(reverse=False)
_print(numbers)
# there's a built in function called sorted, it'll not modify the original list, it'll return sorted list
_print(sorted(numbers))
_print(sorted(numbers, reverse=True))
_print(sorted(numbers, reverse=False))

# Sorting a list of tuples
items = [
    ("itme1", 10),
    ("itme2", 9),
    ("itme3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
_print(items)


# ------------------------------ Lambda functions ------------------------

items = [
    ("itme1", 10),
    ("itme2", 9),
    ("itme3", 12),
]


def sort_item(item):
    return item[1]


# items.sort(key=lambda parameter:expression) # it's like an anonymaous function
items.sort(key=lambda item: item[1], reverse=True)
_print(items)


# ------------------------------ Map functions ------------------------
# Used to transform the data like in JS

# Lets we only wants to get the prices from following array of tuples
items = [
    ("itme1", 10),
    ("itme2", 9),
    ("itme3", 12),
]

prices = map(lambda item: item[1], items)
_print(prices)
_print(list(prices))

# ------------------------------ Filter functions ------------------------
# Used to filter the data like in JS

# Lets we only wants to get the prices from following array of tuples which is greater than 10
items = [
    ("itme1", 10),
    ("itme2", 9),
    ("itme3", 12),
]

prices = filter(lambda item: item[1] >= 10, items)
_print(prices)
_print(list(prices))


# ------------------------------ List Comprehensions ------------------------
# it's the alternative of map and filter function
# [expression for item in item]
# prices = map(lambda item: item[1], items)
prices = [item[1] for item in items]  # this is pretty cleaner
_print(prices)

# prices = filter(lambda item: item[1] >= 10, items)
prices = [item for item in items if item[1] >= 10]  # this is pretty cleaner
_print(prices)


# ------------------------------ Zip Function ------------------------
list1 = [1, 2, 3]
list2 = [4, 5, 6]
#  zip function will combine the two lists in the way that a list of tuples is created
_print(list(zip("abc", list1, list2)))


# ------------------------------ Stacks ------------------------
# LIFO
browsing_sessions = []
browsing_sessions.append(1)
browsing_sessions.append(2)
browsing_sessions.append(3)

_print(browsing_sessions)
browsing_sessions.pop()  # it'll remove last element
_print(browsing_sessions)
browsing_sessions.pop()  # it'll remove last element
_print(browsing_sessions)


# ------------------------------ Stacks ------------------------
# FIFO
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
_print(queue)
queue.popleft()
queue.popleft()
queue.popleft()

_print(queue)

if not queue:
    _print("Empty Queue")


# ------------------------------ Tuples ------------------------
# It's a read only list
# We can not mutate it
# two ways of defining tuples

point = (1, 2)
_print(point)
point = 1, 2
_print(point)
point = (1, 2) * 3
_print(point)
point = (1, 2) + (3, 4)
_print(point)
# converting list to tuples
point = tuple([1, 2])
_print(point)
# converting String to tuples
point = tuple("abc")
_print(point)

x, y, z = point
_print(f"x:{x} y:{y} z:{z}")

# we can access tuples element using index like list
_print(point[0])

if 10 in point:
    _print("Exists")


# ------------------------------ Swapping Variables ------------------------
x = 10
y = 11
y, x = x, y
y, x = (x, y)
y, x = [x, y]

_print(f"x: {x} y: {y}")

# ------------------------------ Arrays ------------------------
# Arrays are used when we use a large sequence of numbers


numbers = array("i", [1, 2, 3])
numbers.append(4)
_print(f"numbers: {numbers}")
numbers.remove(1)
_print(f"numbers: {numbers[1]}")

# ------------------------------ Sets ------------------------
# An unordered collection with no duplicates
numbers = [1, 1, 2, 3, 4, 4, 5]
_print(f"numbers: {numbers}")
unique = set(numbers)
_print(f"unique: {unique}")

numbers_set = {1, 2, 4}
numbers_set.add(5)
numbers_set.remove(5)
_print(f"numbers_set: {numbers_set}")
_print(f"numbers_set length: {len(numbers_set)}")

first = {1, 2, 3}
second = {3, 4}
# Sets union
_print(f"Union: {first | second}")
# Intersaction union
_print(f"Intersaction: {first & second}")
# Difference union
_print(f"Difference: {second - first}")
# semantic Difference | inverse of intersaction. will return only those elements that are not present in both sets
_print(f"semantic Difference: {first ^ second}")

# We can't access them using indexes
if 1 in first:
    _print("Yes")

# ------------------------------ Dictionaries ------------------------
# Dictionaries are powerfull data structures to store key value pairs
# these are unordered collections, we can't sort them values can be accessed by the keys
person = {
    "name": "Usman",
    "gender": "male",
    "age": 29,
    "is_learning": True
}
_print(person.get("name"))
_print(person)
product = dict(name="Jeans", color="Blue",
               length=70, width=35, is_washable=True)
product["quantity"] = 121
_print(product)
_print(product["color"])
_print(product.get("length"))
# accessing key that does not exists, we cam return a default value
_print(product.get("not_exist", "N/A"))

# Another way to get a key that you are not sure about
if "is_on_sale" in product:
    _print(product["is_on_sale"])

del product["width"]
_print(product)

# Loop on dictionary
for key in product:
    _print(f"key: {key} , value: {product.get(key)}")

# Loop on dictionary
for x in product.items():
    _print(f"{x[0]}: {x[1]}")  # it'll return tuple of key and value

# Loop on dictionary
for key, value in product.items():
    _print(f"{key}: {value}")

# ------------------------------ Dictionary comprehensions ------------------------

values = {x * 2 for x in range(5)}  # it's a set comprehensions
_print(values)

values = {x: x * 2 for x in range(5)}  # it's a Dictionary comprehensions
_print(values)

values = (x for x in range(5))  # it's a Tuple comprehensions
_print(values)  # it's returning Generator object


# ------------------------------ Generator Expression ------------------------
# tuple comprehensions return a generator function. we'll get the net value by invoking the generator function. it's a memory efficient way to utilize the data. at start we don't know how many data is generator function going to produce. that's why we can't use len() function on generator function


values = (x for x in range(100000))  # it's a Tuple comprehensions
_print(f"Gen : {getsizeof(values)}")  # size is 104 Bytes

values = [x for x in range(100000)]  # it's a Tuple comprehensions
_print(f"List : {getsizeof(values)}")  # size is 800984 Bytes

# ------------------------------ Unpacking operator ------------------------
# we use it to take out every individual value from every iterable
# it's like spread operator in javascript
# here it's * for un packing
numbers = [1, 2, 3]
# print(*numbers)

values = list(range(5))
_print(values)
values = [*range(5), *"Hello"]
_print(values)

#  we can use this to combine two lists
combined = [*list1, *list2]
_print(combined)

# we can also combine two dictionaries

combined = {**person, **product, "new": True}
_print(combined)


# ------------------------------ Exercise ------------------------
# Find the most repeated character from the text
sentence = "This is a common interview question"

character_frequency = {}

for char in sentence:
    if char in character_frequency:
        character_frequency[char] += 1
    else:
        character_frequency[char] = 1

char_frequency_sorted = sorted(
    character_frequency.items(), 
    key=lambda kv: kv[1], 
    reverse=True
    )
print(char_frequency_sorted[0])
