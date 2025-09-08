#this program displays step by step instructions
#for disassembling an Acme dryer

#the main function displays the programs main logic
def main():
    #display the start-up message
    startup_message()

    #displaying step 1
    input("Press Enter to see step 1.")
    step1()

    #displaying step 2
    input("Press enter to see step 2.")
    step2()

    #displaying step 3
    input("Press enter to see step 3.")
    step3()

    #displaying step 4
    input("Press enter to see step 4")
    step4()


#startup message
def startup_message():
    print("This program tells you how to disassemble the ACME machine")
    print()

#for step 1
def step1 ():
    print("Unplug the dryer and move it away from the wall")
    print()

#for step 2
def step2 ():
    print("Remove the six screws from the back of the dryer")
    print()

#for step 3
def step3 ():
    print("Remove the back panel")
    print()

#for step 4
def step4 ():
    print("Pull the top of the dryer straight up")
    print()

#calling the main to begin the program
main()

