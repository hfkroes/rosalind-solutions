  #Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_hamm.txt', 'r')
text_file = file.read().split('\n')

str1 = text_file[0]
str2 = text_file[1]

#Defining function
def hammingd(str1, str2):
	tmphd = 0
	for i in range(0, len(str1)):
		if not str1[i] == str2[i]:
			tmphd = tmphd + 1
	return tmphd

#Calculating result
res = hammingd(str1,str2)

#Printing hamming distance
print(res)

#Copying to clipboard for easier submition
pyperclip.copy(res)