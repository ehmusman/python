import random
import string
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=2))

# Generating random password
word = "1234567890=-qwertyuiop[]asdfghjkl;'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,./"
password = random.choices(word, k=16)

print("".join(password))


word = string.printable
password = random.choices(word, k=16)

print(word)
print("".join(password))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
random.shuffle(password)
print("".join(password))
print(numbers)