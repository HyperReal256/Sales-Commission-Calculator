'''
program to calculate the BMI (Body Mass Index) of an individual
1. get the weight in kgs
2. get the height in meters
3. calculate the BMI using the formula
4. display the MBI value and the corresponding weight status
'''

patient_name = input("Enter the patient's name: ")     #getting the patient name
weight = float(input("Enter the weight in kgs: "))     #getting the weight of the patient
height = float(input("Enter the height in meters: "))  #getting the height of the patient

#calculating the BMI
bmi = weight / (height ** 2)

#setting the weight status
if bmi < 18.5:
    weight_stautus = "Underweight"
    print(patient_name + " has a BMI of " + str(format(bmi, '.1f') + " and is " + weight_stautus))
elif bmi >= 18.5 and bmi < 24.9:
    weight_stautus = "Normal weight"
    print(patient_name + " has a BMI of " + str(format(bmi, '.1f') + " and is " + weight_stautus))
else:
    weight_stautus ="Overweight"
    print(patient_name + " has a BMI of " + str(format(bmi, '.1f') + " and is " + weight_stautus))