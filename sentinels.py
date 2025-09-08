'''
program to calculate the  property tax
'''

tax_factor = 0.0065

#prompting the user to enter the tax lot number and value of property

print("Enter the property Lot number of 0 to exit")
lot_number = int(input("Enter the Lot number: "))

while lot_number != 0:
    property_value = float(input("Enter the property value: "))
    tax = tax_factor * property_value
    print(f"The tax to be charged on property is {tax:.2f}")

    #or else get the next lot number
    lot_number = int(input("Enter the Lot number or press 0 to exit: "))
