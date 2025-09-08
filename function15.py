'''
program to still demonstrate the use of Return function
'''

DISCOUNT_PERCENTAGE = 0.1

#the main function
def main():
    reg_price = get_regular_price ()    #getting the item's regular price from the retailer
    sale_price = reg_price - discount(reg_price)
    print(f"The sale price is $ {sale_price:,.3f} ")

#function to collect the price tag fo the item
def get_regular_price():
    price = float(input("Enter the regular price of the item: "))
    return price

#function to calculate the discount on the commodity
def discount(price):
    return price * DISCOUNT_PERCENTAGE

#calling the main function
main()