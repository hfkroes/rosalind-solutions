#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_2sum.txt', 'r')
txt_input = file.read().split('\n')

basic_values = txt_input[0].split(' ')
arrays_number = basic_values[0]
limit = int(basic_values[1])

arrays = []
count = 0
for line in txt_input:
   if count > 0:
      arrays.append(line.strip().split(' '))
   count += 1
arrays.remove([''])

#Defining function
def sum2(limit, arrays):
   results = []
   for array in arrays:
      elem_count = {}
      for elem in array:
         elem = int(elem)
         a_elem = abs(elem)
         if a_elem in elem_count:
            if elem < 0:
               elem_count[a_elem] = (elem_count[a_elem][0]+1, elem_count[a_elem][1])
            else:
               elem_count[a_elem] = (elem_count[a_elem][0], elem_count[a_elem][1]+1)
         if elem not in elem_count:
            if elem < 0:
               elem_count[a_elem] = (1, 0)
            else:
               elem_count[a_elem] = (0, 1)
      result_found = False
      n = 0
      for count in elem_count:
         if count == 0 and result_found == False:
            if elem_count[count][1] > 1:
               result_found = True
               a1 = array.index('0') + 1
               a2 = array.index('0', a1, len(array)) + 1
               results.append((a1, a2))
         if elem_count[count][0] > 0 and result_found == False:
            if elem_count[count][1] > 0:
               result_found = True
               a1 = array.index(str(count))+1
               a2 = array.index(str(-1*count))+1
               if a1 < a2:
                  results.append((a1, a2))
               else:
                  results.append((a2, a1))
      if result_found == False:            
         results.append(-1)
   return results

#Obtaining results
res = sum2(limit, arrays)

#Printing result
print('\n'.join(' '.join(str(index).split(', ')).strip("()") for index in res))

#Copying to clipboard for easier submition
pyperclip.copy('\n'.join(' '.join(str(index).split(', ')).strip("()") for index in res))