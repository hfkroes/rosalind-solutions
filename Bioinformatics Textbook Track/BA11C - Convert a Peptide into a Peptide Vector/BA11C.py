#Importing libraries
import pyperclip, itertools

#Aminoacid masses
aa_masses = {"A": 71,"C": 103,"D": 115,
    "E": 129,"F": 147,"G": 57,
    "H": 137,"L": 113,"M": 131,
    "N": 114,"P": 97,"Q": 128,
    "R": 156,"S": 87,"T": 101,
    "V": 99,"W": 186,"Y": 163,
    "I": 113, "K": 128}

#Reading variables txt file
file = open('rosalind_ba11c.txt', 'r')
string = file.read()

#Defining function
def ba11c(string, aa_masses):
	result = []
	for aa in string:
		for index in range(0, aa_masses[aa]-1):
			result.append(0)
		result.append(1)
	return result

#Calculating swaps
res = ba11c(string, aa_masses)

#Printing result
print(' '.join(str(a) for a in res))

#Copying to clipboard for easier submition
pyperclip.copy(' '.join(str(a) for a in res))