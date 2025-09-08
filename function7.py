'''
functions to demonstrate  keywords
'''

def main():
    show_interest(rate = 0.01, period = 10, principal = 1000.0)

def show_interest (principal, period, rate):
    interest = principal * rate * period
    print('The simple interest will be $', format(interest, ',.3f'))

main()