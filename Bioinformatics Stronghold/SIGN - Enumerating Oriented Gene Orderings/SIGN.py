#Importing libraries
import pyperclip, itertools

#Reading variables txt file
file = open('rosalind_sign.txt', 'r')
text_file = file.read()

number = int(text_file[0])

#Defining function
def sign(number):
	results = []
	new_nl = []
	n_list = list(range(1, number + 1))
	for n in n_list:
		new_nl.append(str(n * -1))
	for n in n_list:
		new_nl.append(str(n))
	set = itertools.permutations(new_nl, number)
	for item in list(set):
		item_numbers = []
		rep = False
		for n in item:
			item_numbers.append(abs(int(n)))
		item_numbers = sorted(item_numbers)
		for n in range(number-1):
			if item_numbers[n]==item_numbers[n+1]:
				rep = True
		if rep == False:
			results.append(' '.join(item))
	perm_number = len(results)
	return results, perm_number

#Calculating result
res, pn = sign(number)

#Printing result
print(str(pn)+'\n'+'\n'.join(res))

#Copying to clipboard for easier submition
pyperclip.copy(str(pn)+'\n'+'\n'.join(res))