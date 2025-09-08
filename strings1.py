#program to score students with various grades
#abased on their subject particulars

print("School Report Card Sytem")

#getting user input for four subjects
english_score = float(input("Enter the English score: "))
maths_score = float(input("Enter the Maths score: "))
science_score = float(input("Enter the Science score: "))
sst_score = float(input("Enter the SST score: "))

#calculating the average for the student
average_score = (english_score + maths_score + science_score + sst_score) / 4
average_score_round = format(average_score, '.2f')

#grading the score of reach subject

A_score = 90
B_score = 75
C_score = 60
D_score = 50
E_score = 40
F_score = 0

print("Your average score is " + str(average_score_round))

if sst_score >= A_score:
    print("Your score in SST is " + "A")
elif sst_score >= B_score:
    print("Your score in SST is " + "B")
elif sst_score >= C_score:
    print("Your score in SST " + "C")
elif sst_score >= D_score:
    print("Your score in SST " + "D")
elif sst_score >= E_score:
    print("Your score in SST " + "E")
elif sst_score >= F_score:
    print("Your score in SST " + "F")
else:
    print("The system can't grade your mark!")






