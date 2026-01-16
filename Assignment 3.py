# Factorial using recursion
from numbers import Number


def factorial(n):
   if n == 0 or n == 1:
    return 1
   else:
    return n * factorial(n - 1)

num= float(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")

#Using the Math Module for Calculations

import math

Number= int(input("Enter a number: "))

sqrt_val = math.sqrt(Number)
log_val = math.log(Number)
sine_val = math.sin(Number)

print(f"Square root: {sqrt_val}")
print(f"Logarithm: {log_val}")
print(f"Sine: {sine_val}")
