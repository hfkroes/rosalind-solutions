#Importing libraries
from difflib import SequenceMatcher
import pyperclip

#Reading variables txt file
file = open('rosalind_lcsq.txt', 'r'); sequences = []
lines = file.read().split("\n");
for line in lines:
    if line[0] != ">":
        sequences.append(line)

seq1, seq2 = sequences[0], sequences[1]

#Defining function
def lcs(s1, s2):
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
    cs = matrix[-1][-1]
    return cs

#Printing accordingly
print(lcs(seq1, seq2)) 

#Copying to clipboard for easier submition
pyperclip.copy(lcs(seq1, seq2))