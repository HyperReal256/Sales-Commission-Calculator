'''
program to convert kilometers into miles
'''

#speed conversion expression MPH 5 KPH * 0.6214

print("This program converts kilometers per hpur into miles per hour")
print("KPH" '\t', "MPH")
print("-------------------")

#deploying the for loop
for kph in range (60, 131, 10):
    mph = kph * 0.6214
    mph_1 = format(mph, '.2f')
    print(kph, '\t', mph_1)
