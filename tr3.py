#program to determine legibility of an individual for a loan

'''
conditions to be met
1.  must earn atleast $30,000 per year
2.   must be atleast 2 years at current job
'''

#getting input from the user
salary = float(input("Enter your weekly salary: "))
number_years_worked = int(input("Enter the number of years worked: "))
minimum_salary = 30000    #per year
minimum_work_period = 2
yearly_salary = salary * 12

#making sure the customer fulfills the required requirements
if yearly_salary >= minimum_salary:
    if number_years_worked >= minimum_work_period:
        print("You qualify for the loan")
    else:
        print("You dont qualify for the loan, you must have worked at current place for atleast two years")

else:
    print("Your annual salary must be atleast $", format(minimum_salary, ',.2f') + " to qualify for this loan")

