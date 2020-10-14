#Importing libraries
import pyperclip, itertools

#Reading variables txt file
file = open('rosalind_lexv.txt', 'r')
text_file = file.read().split('\n')

sort_chars = text_file[0].replace(' ', '')
number = int(text_file[1])

#Defining function
def lexv(sort_chars, number):
	results = []
	count = number
	while count > 0:
		set = itertools.product(sort_chars, repeat=count)
		for item in list(set):
			results.append(''.join(item))
		count -= 1
	return results

#Calculating result
res = lexv(sort_chars, number)

#Ordering lexicographically
ordered = sorted(res, key=lambda word: [sort_chars.index(c) for c in word])

#Printing hamming distance
print('\n'.join(ordered))

#Copying to clipboard for easier submition
pyperclip.copy('\n'.join(ordered))