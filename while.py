#usig the while loop

#creating variable to control the loop
keep_going ='Y'

#calculate a series of commisions
while keep_going == 'Y':
    #get salesperson's sales and commission
    sales = float(input("Enter your sales: "))
    commission_rate = float(input("Enter the commission rate: "))

    #calculating the commsission
    commission = sales * commission_rate

    #display the results
    print("Your commission is $" + str(format(commission, ',.2f')) + " for this month")

    keep_going = input("Do you want to continue? Press Y to continue performing the commission calculations: ")
