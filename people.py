'''
sales quota met
'''

sales = float(input("Enter the sales amount:"))

#seeting the sales target
if sales >= 10000:
    sales_target_met = True
else:
    sales_target_met = False

if sales_target_met:
    print("Congratulations, you have hit your sales target!")
else:
    print("You have not hit your sales target")





