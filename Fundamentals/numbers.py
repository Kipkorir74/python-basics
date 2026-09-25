import math
import random
# x = 5
# y = 10.1
# z = 3 + 4j

# print(type(x))  # Output: <class 'int'>
# print(type(y))  # Output: <class 'float'>
# print(type(z))  # Output: <class 'complex'>

# x = 5
# y = 10

# print(complex(x, y))  # Output: (5+10j) Creates a complex number from two numbers using real and imaginary parts.

# Math operators
# print(5 + 3)  # Addition
# print(5 - 3)  # Subtraction
# print(5 * 3)  # Multiplication
# print(5 / 3)  # Division
# print(17 // 3)  # Floor Division divides and returns the largest integer less than or equal to the result
# print(5 % 3)  # Modulus returns the remainder of the division (Detect odd and even numbers)
# print(5 ** 3)  # Exponentiation raises the number to the power of another number

# x = 5
# x = x + 3
# x += 3  # This is equivalent to x = x + 3

# print(x)  # Output: 8

# Rounding
#Measure distance
# print(abs(2-10))  # Output: 8 (absolute value)returns the absolute value of a number, which is the distance from zero on the number line.

# Rounding Numbers
# price = 19.2992312
# print(round(price,2))  # Output: 19.99 (rounds to 2 decimal places)
# print(round(price))  # Output: 19 (rounds to the nearest integer)
# print(math.floor(price))  # Output: 19 (rounds down to the nearest integer)
# print(math.ceil(price))  # Output: 20 (rounds up to the nearest integer)
# print(math.trunc(price))  # Output: 19 (truncates the decimal part, effectively rounding towards zero)
# print(int(price))  # Output: 19 (converts the float to an integer, effectively truncating the decimal part)

# Random Numbers


# # Generate a random integer between 1 and 10 (inclusive)
# print(random.randint(4, 100))

# # Generate a random float between 0 and 1
# print(random.random())

# Validate a number
# x = 10.000
# y = 5.5
# print(x.is_integer())  # Output: True (checks if the number is an integer)
# print(y.is_integer())  # Output: False (checks if the number is an integer)

# x = 87.4

# print(isinstance(x, int))  # Output: False (checks if x is an instance of the int class)
# print(isinstance(x, float))  # Output: True (checks if x is an instance of the float class)
# # isinstance() check if a value belongs to a specific data type or class. It returns True if the value is an instance of the specified class, and False otherwise.

# x = random.randint(1, 100)  # Output: A random integer between 1 and 100 (inclusive)
# print(x)
# print(x % 2 == 0)  # Output: True if x is even, False if x is odd