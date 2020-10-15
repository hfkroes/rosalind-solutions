#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_maj.txt', 'r')
txt_input = file.read().split('\n')

basic_values = txt_input[0].split(' ')
arrays_number = basic_values[0]
limit = basic_values[1]

arrays = []
count = 0
for line in txt_input:
   if count > 0:
      arrays.append(line.split(' '))
   count += 1
arrays.remove([''])

#Defining function
def maj(arrays_number, limit, arrays):
   results = []
   array_count = 1
   for array in arrays:
      elem_count = {}
      for elem in array:
         if elem in elem_count:
            elem_count[elem] += 1
         if elem not in elem_count:
            elem_count[elem] = 1
      result_found = False
      for count in elem_count:
         if int(elem_count[count]) > int(limit)/2 and result_found == False:
            results.append(count)
            result_found = True
      if result_found == False:
         results.append(-1)
      array_count += 1
   return results

#Obtaining results
res = maj(arrays_number, limit, arrays)

#Printing result
print(' '.join(str(index) for index in res))

#Copying to clipboard for easier submition
pyperclip.copy(' '.join(str(index) for index in res))