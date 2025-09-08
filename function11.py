#program to display random numbers

import random

#creating a function that generates random numbers
def main():
    for count in range(5):
        print(random.randint(1003,9000))

#calling the main function
main()