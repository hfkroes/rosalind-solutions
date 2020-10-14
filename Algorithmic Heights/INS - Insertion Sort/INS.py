#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_ins.txt', 'r')
variables = file.read().split('\n')

length = int(variables[0])
numbers = (variables[1]).split(' ')
int_numbers = []

for number in numbers:
   int_numbers.append(int(number))

#Defining function
def ins(length, numbers):
   swaps = 0
   for i in range(1, length):
      key = numbers[i]
      j = i-1
      while j >=0 and key < numbers[j] :
         numbers[j+1] = numbers[j]
         j -= 1
         swaps += 1
      numbers[j+1] = key
   return swaps, numbers

#Calculating swaps
swaps, res_numbers = ins(length, int_numbers)

#Printing result
print(str(swaps))

#Copying to clipboard for easier submition
pyperclip.copy(swaps)