'''
program to demonstrate use of global constants
'''

#the contribution rate constant

CONTRIBUTION_RATE = 0.05

#creating the main function to hold all other functions
def main():
    gross_pay = float(input('Enter the gross pay: '))

    #checking the entry made by the user
    while gross_pay < 0:
        print('Gross pay cannot be less than zero')
        gross_pay = float(input('Please enter your gross pay again: '))

    bonus = float(input('Enter the amount of bonuses: '))
    while bonus < 0:
        print('Bonus pay cannot be less than zero!')
        bonus = float(input('Enter your bonus pay again: '))
   

    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

#creating the gross pay contribution function
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay is $', format(contrib, ',.2f'))

def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f"The contribution for bonuses is {contrib:,.2f}")

#calling the main function
main()