'''
program to calculate for the number of cups of each of the following ingredients
1.  sugar (1.5)
2. butter (1)
3. flour(2.75)

the above ingredients are needed to make 48 cookies
'''


#getting the number of cookies that the user wants to make
number_of_cookies = int(input("Enter the number of cookies that you want make: "))

#calculating the number of cups of each ingredient to use
sugar = ((1.5 / 48) * number_of_cookies)
butter = ((1 / 48) * number_of_cookies)
flour = ((2.75 / 48)* number_of_cookies)

#rounding off to the 2dp
sugar_1 = format(sugar, '.2f')
butter_1 = format(butter, '.2f')
flour_1 = format(flour, '.2f')

#displaying the quantities of ingredients to be used
print("You will need " + str(sugar_1) + " cups of sugar, " + str(butter_1) + " cups of butter and " + str(flour_1)+ " cups of flour")
