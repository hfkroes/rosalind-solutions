#Importing libraries
import pyperclip, math

#Reading variables txt file
file = open('rosalind_afrq.txt', 'r')
input_file = file.read().split(' ')

def probs(rec_hom_freq):
	allele_freq = math.sqrt(rec_hom_freq)
	compl_value = 1 - allele_freq
	return((allele_freq**2)+2*(allele_freq*compl_value))

results = []
for i in input_file:
	results.append(probs(float(i)))

#Printing results
print(' '.join([str(i) for i in results]))