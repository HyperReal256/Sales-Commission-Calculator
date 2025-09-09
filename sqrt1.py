import math

number = int(input("Enter a number to find its square root:"))

def number_sqrt(number):
    sqrt_1 = math.sqrt(number)
    print(f"The square root of {number} is {sqrt_1}")

number_sqrt(number)
