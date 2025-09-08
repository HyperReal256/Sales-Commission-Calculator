'''
function to simulate rolling of a dice
'''

#importing the random modules

import random

#creating constants for the min and max values
MAX = 6
MIN = 1

def main():
    #creating a variable to control the loop
    again = 'y'

    while again == 'y' or again =='Y':
        print('Dice is rolling')
        print('The values are: ')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        #asking the use if he wants to continue rollinf the dice
        again = input("Enter 'y' to continue playing: ")

#calling the main function
main()
       
