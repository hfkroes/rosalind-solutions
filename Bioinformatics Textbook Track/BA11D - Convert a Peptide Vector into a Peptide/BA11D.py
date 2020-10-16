#Importing libraries
import pyperclip

#Aminoacid masses
aa_masses = {"A": 71,"C": 103,"D": 115,
    "E": 129,"F": 147,"G": 57,
    "H": 137,"L": 113,"M": 131,
    "N": 114,"P": 97,"Q": 128,
    "R": 156,"S": 87,"T": 101,
    "V": 99,"W": 186,"Y": 163}

#Reading variables txt file
file = open('rosalind_ba11d.txt', 'r')
array = file.read()

mass_array = []
for elem in array.replace(' ', '').split('1'):
	mass_array.append((len(elem)+1))

#Defining function
def ba11d(length, numbers):
	string = []
	for mass in mass_array:
		aa_found = False
		for aa in aa_masses:
			print(mass, aa_masses[aa], aa)
			if mass == aa_masses[aa] and aa_found == False:
				string.append(aa)
				aa_found = True
	return ''.join(string)

#Calculating swaps
res = ba11d(mass_array, aa_masses)

#Printing result
print(res)

#Copying to clipboard for easier submition
pyperclip.copy(res)