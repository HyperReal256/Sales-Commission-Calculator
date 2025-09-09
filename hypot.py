#program to calculate the hypotenuse 
import math

#getting the lenths of the two side
def main():
    side_a = float(input("Enter the length of side A; "))
    side_b = float(input("Enter the length of side B; "))

    #calculating the hyp 
    hypotenuse = math.hypot(side_a, side_b)

    #printing the hyp
    print("The lenghth of the hypotenuse is:", hypotenuse)

main()