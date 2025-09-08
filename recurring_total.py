
'''
Program to claculate the total of a series of entries entered by the user
'''

#ask the user how many entries they want to make
max_number = int(input("How many numbers do you want to add? "))

total = 0.0     #initializing the total variable

#calling the for loop
for count in range (max_number):
    number = float(input(f"Enter number {count+1}: "))   #getting a number from the user
    total += number    #calculating the total
    print(f"The total so far is {total:.2f}")   #displaying the current totals

#final result
print(f"\nThe final total after {max_number} numbers is {total:.2f}")
