'''
Write a program that asks the user for a DNA sequence 
and prints whether its length is greater than 10 nucleotides.
'''

#getting user input
dna_sequence = input("Enter a DNA sequence: ")

#checking the lenght of the DNA sequence
if len(dna_sequence) > 10 and len(dna_sequence) % 3 == 0:
    print("The length of the DNA sequence is greater than 10 nucleotides and does code for a protein")
else:
    print("The lenght of the DNA sequence is not greater than 10 nucleotides")