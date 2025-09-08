'''
program that displays the day of the week given a number between 1 and 7
1. get a number from user betwwen 1 and 7
2. display the corresponding day of the week
3. if the number is out of range, display an error message
'''

#getting user input
day_number = int(input("Enter a number between 1 and 7: "))

#setting the days of the week
day_1 = "Monday"
day_2 = "Tuesday"
day_3 = "Wednesday"
day_4 = "Thursady"
day_5 = "Friday"
day_6 = "Saturday"
day_7 = "Sunday"

#displaying the corresponding day of the week
if day_number < 1 or day_number > 7:
    print("Error, number is out of range!")
elif day_number == 1:
    print("The day is "+ day_1)
elif day_number == 2:
    print("The day is " + day_2)
elif day_number == 3:
    print("The day is " + day_3)
elif day_number == 4:
    print("The day is " + day_4)
elif day_number == 5:
    print("The day is " + day_5)
elif day_number == 6:
    print("The day is " + day_6)
else:
    print("The day is " + day_7)
