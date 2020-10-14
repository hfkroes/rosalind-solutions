#Importing libraries
import pyperclip, requests
from bs4 import BeautifulSoup

#Reading variables txt file
file = open('rosalind_dbpr.txt', 'r')
pdb_id = file.read()

#Defining function
def dbpr(pdb_id):
	loi = []
	page = requests.get(f"http://www.uniprot.org/uniprot/{pdb_id}.txt")
	page_parsed = BeautifulSoup(page.text, 'html.parser')
	lines = str(page_parsed).split('\n')
	for line in lines:
		if line[0:8] == "DR   GO;":
			loi.append(line)
	eoi = []
	for line in loi:
		elements = line.split(':')
		if elements[1][-1] == 'P':
			eoi.append(elements[2].split(';')[0])
	return eoi

#Calculating result
res = dbpr(pdb_id)

#Printing result
print('\n'.join(res))

#Copying to clipboard for easier submition
pyperclip.copy('\n'.join(res))
