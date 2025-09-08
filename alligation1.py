'''
Program to do alligation calculations
'''

#creating the main functions to call other functions




#building the function to handle two stock solutions
def alligation_2():


    def user_1_input():
        #requesting for input from user
        solution_1 = float(input("Enter your first stock solution strength: "))      
        while solution_1 < 0:          #checking the validity of the input
            print("Strength of stock Solution-1 cannot be negative. Please correct it!")
            solution_1 = float(input("Enter your first stock solution strength again: "))
        return solution_1

    def user_2_input():
        #getting the second stock solution strength from user
        solution_2 = float(input("Enter your second stock solution strength: "))
        while solution_2 < 0:
            print("Strenth of stock Solutiom-2 cannot be negative, Please correct it!")
            solution_2 = float(input("Enter your second stock solution strength again: "))
        return solution_2
        
    def user_target_strength():
        #getting the target strength from the user
        target_strength = float(input("Enter your target strength: "))
        while target_strength < 0:
            print("Target strength cannot be negative, Please correct it!")
            target_strength = float(input("Enter your target strength again: "))
        return target_strength

    s1 = user_1_input()
    s2 = user_2_input()
    c = user_target_strength()

    #checking if the target strength lies between the two stock solutions
    while not (s1 <= c <= s2):
        print(f"The target strength {c} must lie between the two stock solutions {s1} and {s2}")
        c = int(input("Enter your target strength again: "))


    def parts():
        #calculating the parts of stock solutions 1 and 2
        part_1 = abs(s2 - c)
        part_2 = abs(s1 - c)
        print(f"Parts of stock Solution-1 = {part_1} and parts of stock Solution-2 = {part_2}")
        return part_1, part_2

   #calculating for the total volumes
    def volume():
        #getting the total volume required
        total_volume = int(input("Enter your total volume required for the dose in mL: "))
        while total_volume <= 0:
            print("Total volume cannot be zero or negative!")
            total_volume = int(input("Enter your total volume required: "))
        return total_volume

    #obtaining the parts of stock solutions 1 and 2
    part_1, part_2 = parts()
    total_parts = part_1 + part_2
    total_volume = volume()

    #calculating the volumes of stock solution_1
    volume_1 = (part_1 / total_parts) * total_volume
    volume_2 = (part_2 / total_parts) * total_volume

    #printing the results
    print(f"Your are going to use {volume_1:.2f} mL of stock solution-1")
    print(f"Your are going to use {volume_2:.2f} mL of stock solution-2")

#callling the function
alligation_2()

    