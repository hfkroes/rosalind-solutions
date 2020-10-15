#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_mer.txt', 'r')
txt_input = file.read().split('\n')

array1 = txt_input[1].split(' ')
array2 = txt_input[3].split(' ')

#Defining function
def mer(array1, array2):
   array3 = []
   for item in array1:
      array3.append(int(item))
   for item in array2:
      array3.append(int(item))
   return sorted(array3)

#Calculating results
array3 = mer(array1, array2)

#Printing result
print(' '.join(str(item) for item in array3))

#Copying to clipboard for easier submition
pyperclip.copy(' '.join(str(item) for item in array3))