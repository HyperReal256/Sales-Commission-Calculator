'''
program to calculate the gross pay of each individual worker
'''

hours_worked = int(input("Enter number of hours worked in a week: "))
hour_pay_rate = float(input("Enter the hourly payrate: "))

#calculating the gross income
gross_income = hour_pay_rate * hours_worked


if hours_worked <= 40:
    print("Your gross pay is " + str(gross_income))

else:
    overtime = hours_worked - 40
    gross_pay_plus = (hour_pay_rate * 40)
    overtime_pay = (overtime * (1.5 * hour_pay_rate))
    final_pay = overtime_pay + gross_pay_plus
    print("Your weekly pay is " + str(final_pay))

