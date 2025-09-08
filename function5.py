#this program converts cups to fluid ounces

def main():
    #displat intro message
    intro()

    #getting the number of cups
    cups_needed = int(input("Enter the number of cups needed: "))

    #passing this as an argument to the cups_to_ounce function
    cups_to_ounce (cups_needed)

#this is a function to dislay the into message
def intro():
    print('This program converts measurements of cups to fluid ounces')
    print('1 cup = 8 fluid ounces')

#function that does the computation
def cups_to_ounce(cups_needed):
    ounces = cups_needed * 8
    print("That converts to ", ounces, 'ounces')

#calling the main function
main()