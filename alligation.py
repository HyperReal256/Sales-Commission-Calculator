"""Bulding a function, alical(s1,s2,C,V), to perform alligation alternate.
arguments:-
s1-strength of stock solution1,
s2-strength of stock solution2,
C-the desired target concentration of solution to be prepared,
V-the target volume of solution to be prepared,

if V=0 then alical(s1,s2,C,V) should output:-
p1, the parts of stock solution 1 to be measured
p2, the parts of stock solution 2 to be measured

otherwise alical(s1,s2,C,V) should output:-
vol1 the volume of stock solution 1 to be measured
vol2 the volume of stock solution 2 to be measured

Other restrictions to the values of arguments passed into the function when called have been defined as below"""

"""
asking the user to input the number of stock solutions that they intend to use
this line of code helps to call the various functions of either two or three stock solutions to be used depending on the user's input
"""

try:
    number_of_solns = int(input("Program accomodates only 2 and 3 solutions, how many stock solutions do you intend to use:  "))
    if number_of_solns == 0:
        print("Invalid user input.")

    elif number_of_solns == 1:
        print("You need more than one solution to perform alligation computations.")

    elif number_of_solns == 2:

        s1 = float(input("Enter your first stock solution strength: "))

        s2 = float(input("Enter your second stock solution strength: "))

        C = float(input("Enter your target strength: "))

        V = int(input("Enter your total volume required for the dose: "))

        def alical():

            # Parts of stock solutions 1 & 2
            p1 = abs(s2 - C)
            p2 = abs(s1 - C)

            # Volumes of stock solutions 1 & 2
            vol_1 = (p1 / (p1 + p2)) * V
            vol_2 = (p2 / (p1 + p2)) * V

            # integer casting t give rounded off values
            vol_1 = int(vol_1)
            vol_2 = int(vol_2)
            # Restrictions on arguments to be passed into the function upon invocation/calling of the function

            # print("Only real number values are acceptable as inputs. Please correct inputs that do not comply!")
            if s1 < 0:
                print("Strength of Stock solution1,", s1,
                      "is negative. This is not physically possible. Please check and correct it!")
            elif s2 < 0:
                print("Strength of Stock solution2,", s2,
                      "is negative. This is not physically possible. Please check and correct it!")
            elif C < s1 or C > s2:
                print("Your target strength must lie between", s1, "and", s2)
            elif V < 0:
                print("A negative volume such as", V, "is not physically possible. Please correct!")
            elif V == 0:
                print("Parts of stock Solution1=", p1)
                print("Parts of stock Solution2=", p2)
            else:
                print("Volume of stock solution1=", vol_1)
                print("Volume of stock solution2=", vol_2)
        alical()

    elif number_of_solns == 3:
        """
        Under the following codes, we shall be calculating ratios/proportions for 3 conc solutions
        The conc solutions to be used: s_1, s_2 and s_3 must be arranged in ascending order.
        This is for convinience for the system as we await for further system modifications
        """

        def alical_1():
            # getting input from the user, remember we are using 3 conc solutions
            s_1 = float(input("Enter your first stock solution strength: "))

            s_2 = float(input("Enter your second stock solution strength: "))

            s_3 = float(input("Enter your third stock solution strength: "))

            C_1 = float(input("Enter your target strength: "))

            V_1 = float(input("Enter your total volume required for the dose: "))

            """
            calculating parts for each solution: s1, s2, and s3
            considering s_2 to be greater than C_1
            """

            if s_1 < C_1 < s_2:
                p3 = abs(s_1 - C_1)
                p4 = abs(s_2 - C_1)
                # checking if s2 is greater than C and if true then, we are to perform the following computations
                if s_2 > C_1:
                    pl = abs(s_3 - C_1)
                    pm = abs(s_1 - C_1)
                    print(p3, p4 + pl, pm)

                    # Volumes of stock solutions 1, 2 and 3
                    vol1 = ((p4 + pl) / (p4 + pl + p3 + pm)) * V_1
                    vol2 = (p3 / (p4 + pl + p3 + pm)) * V_1
                    vol3 = (pm / (p4 + pl + p3 + pm)) * V_1

                    # calculating the volumes of the various solutions to be used
                    print("Volume of stock solution One =", vol1)
                    print("Volume of stock solution Two =", vol2)
                    print("Volume of stock solution Three =", vol3)
                    # Restrictions on arguments to be passed into the function upon invocation/calling of the function

                else:
                    print("Sorry can't solve this. this may due invalid data input, please check your input and try later.")

            # considering when C_1 is greater the s_2
            elif s_2 < C_1 and s_3 > C_1:
                p5 = abs(s_3 - C_1)
                p6 = abs(s_3 - C_1)
                p7 = abs(s_1 - C_1)
                pt = abs(s_2 - C_1)
                add_two = p7 + pt
                print(p6, p5, add_two)

                # Volumes of stock solutions 1, 2 and 3
                vol4 = (p6 / (p6 + p5 + p7 + pt)) * V_1
                vol5 = (p5 / (p6 + p5 + p7 + pt)) * V_1
                vol6 = ((p7 + pt) / (p6 + p5 + p7 + pt)) * V_1

                # calculating the volumes of the various solutions to be used
                print("Volume of stock solution One =", vol4)
                print("Volume of stock solution Two =", vol5)
                print("Volume of stock solution Three =", vol6)
            # dealing with the second and third conc solutions; s2 and s3
            else:
                print("Sorry can't make this computation.")
        alical_1()
    else:
        print("Dear Pharmacist, the system cannot accomodate your number of solutions to be used, please kindly wait any future system upgrades.")

#raising exceptions for invalid input from the user
except ValueError:
    print("Please use integer or float values only, other characters are not accepted!")
except NameError:
    print("Invalid input from the user")
except Exception as e:
    print(e)
finally:
    print("Thanks for using the Pharm-Formulator Software!")