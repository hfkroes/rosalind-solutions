#Importing libraries
import pyperclip, math

#Reading variables txt file
file = open('rosalind_aspc.txt', 'r')
input_file = file.read().split(' ')

n = int(input_file[0]); m = int(input_file[1]);
k = n; result = 0

result = sum(math.comb(n, k) for k in range(m, n+1)) % 1000000

#Printing result
print(result)

#Copying to clipboard for easier submition
pyperclip.copy(result)