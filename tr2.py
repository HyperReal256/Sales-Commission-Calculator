'''
1. Get the original price of the item.
2. Calculate 20 percent of the original price. This is the amount of the discount.
3. Subtract the discount from the original price. This is the sale price.
4. Display the sale price.
'''

#creating variable to store original price of the commodity
original_price = float(input("Enter the original price of item: "))
percent_discount = float(input("Enter the discount percentage: "))

#calculating the discount amount abased on the original price
discount_amount = (percent_discount / 100) * original_price

#calcculating the new sale price
sale_price = original_price - discount_amount

#displaying the sale price
print("The new sale price of the item is $" + format(sale_price, '4,.2f'))

#percentage increase in the price of the item
percentage_increase = (discount_amount / original_price)
print('The percentage increase is ' + format(percentage_increase, '.0%'))