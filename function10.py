#this program generates random number

import random

#creating a function that generates random numbers
def main():
    #getting a random number
    number = random.randint(1, 20)
    #displaying the number
    print('The number is ', number)

#calling the function
main()