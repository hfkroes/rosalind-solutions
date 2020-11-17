#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_rstr.txt', 'r')
input_file = file.read().split('\n')

n, x = input_file[0].split(' ')
string = input_file[1]

#Building function
def prob(n, gc, seq):
    percent = 1
    prob_gc = gc/2
    prob_at = (1-gc)/2
    for i in seq:
        if i == 'G' or i == 'C':
            percent *= prob_gc
        elif i == 'A' or i == 'T':
            percent *= prob_at
    percent = 1 - (1 - percent) ** n
    return percent

#Calculating probability
res = prob(n, x, string)

#Printing result
print("%.3f" % res)

#Copying to clipboard for easier submition
pyperclip.copy("%.3f" % res)
