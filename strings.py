'''
program to check for teh validity of a password
'''

#getting the user password
password = input("Enter your password: ")

#prompting the system to verify the password
system_password = "Gabula256!"
if password == system_password:
    print("Login successful")
else:
    print("You have entered the wrong password")