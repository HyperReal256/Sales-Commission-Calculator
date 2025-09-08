'''
loan calculator revisited
'''

#setting up the constants
minimum_salary = 30000   #per year
minumum_work_period = 2  #minimum number of years worked at current job


#getting user input
salary = float(input("Enter your yearly salary: "))
number_of_years_worked = int(input("Enter the number of years worked:"))

#checking if the user qualifies for the loan
if salary < minimum_salary:
    print("You must earn atleast $", format(minimum_salary, ',.2f') + " per year to qualify for this loan")
elif number_of_years_worked < minumum_work_period:
    print("You must have worked at your current job for atleast ", minumum_work_period, " years to qualfy for this loan")
elif salary >= minimum_salary and number_of_years_worked >= minumum_work_period:
    print("You qualify for the loan")
else:
    print("You don't qualify for this loan")