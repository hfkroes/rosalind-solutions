#Importing libraries
import pyperclip, math

#Reading variables txt file
file = open('rosalind_prob.txt', 'r')
input_file = file.read().split('\n')

string = input_file[0]
probs = input_file[1].split(' ')

int_probs = []
for p in probs:
	int_probs.append(float(p))

#Building frequency dictionary
nuc_count = {}
nuc_count['A/T'] = 0; nuc_count['G/C'] = 0
for char in string:
	if char == 'G' or char == 'C':
		nuc_count['G/C'] += 1
	else:
		nuc_count['A/T'] += 1

#Defining function
def prob(nuc_count, probs):
	prob_list = []
	for index in range(0, len(probs)):
		log_probs = math.log(((probs[index]/2)**nuc_count['G/C'])*(((1-probs[index])/2)**nuc_count['A/T']), 10)
		prob_list.append(log_probs)
	return prob_list

#Calculating swaps
res = prob(nuc_count, int_probs)
log_list = [str(l)[0:7] for l in res]

#Printing result
print(' '.join(log_list))

#Copying to clipboard for easier submition
pyperclip.copy(' '.join(log_list))