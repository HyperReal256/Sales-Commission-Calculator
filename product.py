numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

if denominator == 0:
    print("Division by zero is not possible")
    denominator = int(input("Enter the denominator again: "))
    
else:
    division = numerator / denominator
    print(f"The result of the division is {division:.2f}")