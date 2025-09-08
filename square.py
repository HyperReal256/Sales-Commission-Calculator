'''
program which gets a numbers (in a given range) from the user and prints its square
'''

print("This program displays the square of numbers entered by the user")
start_num = int(input("Enter the starting number: "))    #getting the starting number from the user
end_num = int(input("Enter the ending number: "))     #getting the ending number from the user

#creating a table to display the numbers and their squares
print("Number", '\t', "Square")
print("------------------")

if start_num < end_num:     #checking if the starting number is less than the ending number
    for num in range (start_num, end_num + 1):
        square = num ** 2
        print(num, '\t', square)
else:
    print("The starting number should be less than the ending number")