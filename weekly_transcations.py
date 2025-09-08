'''
program to calculate the cumulative sales of the business
'''

#getting the user input on the number of transactions made that day
number_transcation = int(input("Enter the number of transcations made: "))

#initiating the totals variable
total_sales = 0.0

#iterating and capturing the number of transcations and total
for count in range (number_transcation):
    number = float(input("Enter amount here: "))
    total_sales += number
    print(f"\nYour cumulative sales amount is {total_sales:.2f}")