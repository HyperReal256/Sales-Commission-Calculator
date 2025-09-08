'''
Algorithm: Student Average Marks Program

Start

Ask the user to enter the number of students → store in num_students.

Ask the user to enter the number of exams per student → store in num_exams.

For each student (repeat num_students times):
a. Set total = 0.
b. Display the student number.
c. For each exam (repeat num_exams times):
i. Ask the user to enter the exam mark.
ii. Add the mark to total.
d. Calculate average = total / num_exams.
e. Display the student number and their average mark.

'''

#entering the number of students
num_students = int(input("Enter the number of students: "))

#entering the number of exams the students sat for
num_exams = int(input("Enter the number of exams each student sat for: "))

#looping through each student
for student in range (num_students):
    total = 0.0         #initializing the total variable
    print(f"\nStudent {student + 1}")    #dispalying the student number
    print("-------------")

    #looping through each exam for the students
    for exam in range (num_exams):
        mark = float(input(f"Enter mark for the exam {exam + 1}: "))      #getting the mark for each test

        #scoring the total marks
        total += mark

        #calculating the average mark
        average = total / num_exams

        #printing the average mark for each student
        print(f"The average mark for student {student + 1} is {average:.2f}")


