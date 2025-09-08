numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

#validating the denominator
while denominator == 0:
    print("Division is not possible!")
    denominator = int(input("Enter a non-zero digit: "))

division = numerator / denominator

#printing the result of the division
print(f"The result of the division of {numerator} and {denominator} is {division}")

