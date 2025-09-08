'''
Program to convert seconds into hour/minutes/seconds formal

1. input from the user the number of seconds
2. calculate the number of hours, minutes and seconds
3. display the result in the formal HH:MM:SS

dwelling on the problem; from 2
1. calculating the number of hours (divide the number of seconds by 3600)
2. obtain the remaininf seconds (use the % operator)
3. calculate the number of minutes (divide the remaning seconds by 60)
4. obtain the remaining seconds (use the % operator again)
5. display the result in the the required format

'''

#program to convert seconds into hour:minutes:seconds format



seconds = float(input("Enter the number of seconds: ")) #getting user input

number_of_hours = seconds // 3600       #calculating the number of hours
remaining_seconds = seconds % 3600      #getting the number of remaining seconds
number_of_minutes = remaining_seconds // 60  #calculating the number of minutes
remaining_seconds_1 = remaining_seconds % 60  #reamining seconds

print("Hours: " + str(number_of_hours))
print("Minutes: " + str(number_of_minutes))
print("Seconds: " + format(remaining_seconds_1, '.3f'))

