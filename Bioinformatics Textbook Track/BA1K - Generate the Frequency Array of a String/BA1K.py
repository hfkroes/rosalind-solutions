#Importing libraries
import pyperclip, itertools

#Reading variables txt file
file = open('rosalind_ba1k.txt', 'r')
input_file = file.read().split('\n')

string = input_file[0]
k = int(input_file[1])
l = len(string)

#Building k-mer dictionary
kmer_list = [''.join(kmer) for kmer in itertools.product('ACGT', repeat = k)]
kmer_count = {}
for kmer in kmer_list:
	kmer_count[kmer] = 0

#Defining function
def ba1k(string, kmer_count, k, l):
	for init in range(0, l-k+1):
		kmer_count[string[init: init+k]] += 1
	return kmer_count

#Calculating swaps
res = ba1k(string, kmer_count, k, l)
freq = [str(res[kmer]) for kmer in res]

#Printing result
print(' '.join(freq))

#Copying to clipboard for easier submition
pyperclip.copy(' '.join(freq))