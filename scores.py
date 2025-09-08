'''
calculatin the average scores of a student and throwing a comment it
z
'''

#getting the test results
test_1 = int(input('Enter the score for the first test: '))
test_2 = int(input('Enter the score for the second test: '))
test_3 = int(input('Enter the score for the third test: '))

#calculating the average for the scores entered
average_score = ((test_1 + test_2 + test_3) / 3)
average_score_roundoff = format(average_score, '.2f')

print("Your average score in the three tests was ", average_score_roundoff)

if average_score >= 95:
    print("Congratulations upon your excellent scores")
else:
    print("Keep up and aim for higher scores")