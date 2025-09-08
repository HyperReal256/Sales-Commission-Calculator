'''
program to calculate the retail prices of commodities
'''

markup = 2.5

#getting input from the user
print("This program calculates the retail prices of goods")

another = 'y'

while another == 'y':
    wholesale_price = float(input("Enter the wholesale price of the item: "))

    #validating the user input
    while wholesale_price < 0:
        print("Error! The price cannot be a negative")
        wholesale_price = float(input("Enter the wholesale price again: "))

    retail = wholesale_price * markup

    #displaying the retail price
    print("The retail price of the item is ", str(format(retail, ',.2f')))

    #asking for another item 
    another = input("Do you have another item to add? Press Y to continue: ")

    

    
    