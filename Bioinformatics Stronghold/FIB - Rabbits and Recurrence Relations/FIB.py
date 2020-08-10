#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_fib.txt', 'r')

variables = file.read().split(' ')
n = int(variables[0])
k = int(variables[1])

#Defining function
def rabbit(n, k):
	if n==1 or n==2:
		return 1
	else:
		return (rabbit(n-1, k)+(k*(rabbit(n-2, k))))

#Calculating rabbit number
rabbit_number = rabbit(n, k)

#Printing accordingly
print(rabbit_number)

#Copying to clipboard for easier submition
pyperclip.copy(rabbit_number)
