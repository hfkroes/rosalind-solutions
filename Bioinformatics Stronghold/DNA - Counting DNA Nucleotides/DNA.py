#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_dna.txt', 'r')
dna_string = file.read().strip()

#Counting
nucleotide_counter = {}
for base in dna_string:
	if base in nucleotide_counter:
		nucleotide_counter[base] += 1
	else:
		nucleotide_counter[base] = 1

#Printing accordingly
print(nucleotide_counter['A'], nucleotide_counter['C'], nucleotide_counter['G'], nucleotide_counter['T'])

#Copying to clipboard for easier submition
pyperclip.copy(nucleotide_counter['A'], nucleotide_counter['C'], nucleotide_counter['G'], nucleotide_counter['T'])