#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_ba1l.txt', 'r')
string = (file.read().rstrip())[::-1]

#Defining dictionary
dictionary = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

#Calculating n
n = 0
for i in range(len(string)):
    n += dictionary[string[i]] * 4 ** i

#Printing result and copying to clipboard
pyperclip.copy(n)
print(n)