#program to assist technicain in monitoring the temp 

#getting the user input of the temperature
substance_temp = float(input("Enter the substance temperature: "))

#bringing in the iteration to check if the temp is within normal ranges

temperature = 102.5

while substance_temp > temperature:
    print("Turn down the thermostat, wait for 5 minutes and check the tempearture again")
    substance_temp = float(input("Enter the new temperature: "))

#print the outcome if the temp passes
print("The temperature is acceptable")
print("Check it agin in 15 minutes!")