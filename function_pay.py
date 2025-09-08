'''
this program calculates a sales person's pay
'''

#definiing the main functions to handle the rest of the functions
def main():
    #getting the amount of sales
    sales = get_sales()

    #get amount of advance pay taken by the salesperson
    advance_pay = get_advance_pay()

    #determine the commission rate
    comm_rate = determine_comm_rate(sales)

    #calculating the net pay
    pay = sales * comm_rate - advance_pay

    #display the amount to pay
    print(f"The pay is ${pay:,.2f}")

    #determine whether the pay is negative
    if pay < 0:
        print("The salesperson must reimburse the company!")

#function to get the amount of sales
def get_sales():
    monthly_sales = get_valid_input("Enter the amount of sales in $: ", min_value=0)
    return monthly_sales      #returning the value entered

#function to get the advance pay
def get_advance_pay():
    advance = get_valid_input("Enter the amount of advance pay taken by the salesperson: ", Max_value = 15000)
    return advance

#function to determine the commission rate
def determine_comm_rate(sales):
    if sales < 10000:
        rate = 0.10
    elif sales >= 10000 and sales < 14999.99:
        rate = 0.12
    elif 15000 <= sales < 17999.99:
        rate = 0.14
    elif 18000 <= sales < 21999.99:
        rate = 0.16
    else:
        rate = 0.18
    #calling the rate
    return rate


#input validation code

def get_valid_input(prompt, min_value=None, Max_value=None):
    while True:
        try:
            value = float(input(prompt)) #ask user input
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Try again!")
                continue
            if Max_value is not None and value > Max_value:
                print(f"Value must be at most {Max_value}. Try again!")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


#calling the main function 
main()