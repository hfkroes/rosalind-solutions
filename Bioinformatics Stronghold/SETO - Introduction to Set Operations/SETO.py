#Importing libraries
import pyperclip, re

#Reading variables txt file
file = open('rosalind_seto.txt', 'r')
text_file = file.read().split('\n')

n = int(text_file[0])
set1 = set([int(i) for i in re.sub("[{}]", "", text_file[1]).split(', ')])
set2 = set([int(i) for i in re.sub("[{}]", "", text_file[2]).split(', ')])
setn = set([i for i in range(1, n+1)])

#Defining function
def seto(set1, set2, setn):
	set_union = set1|set2
	set_intersec = set1&set2
	set_diff_12 = set1-set2
	set_diff_21 = set2-set1
	set1_comp = setn-set1
	set2_comp = setn-set2
	return set_union, set_intersec, set_diff_12, set_diff_21, set1_comp, set2_comp

#Calculating sets
set_union, set_intersec, set_diff_12, set_diff_21, set1_comp, set2_comp = seto(set1, set2, setn)

#Printing sets
print(f"{set_union}\n{set_intersec}\n{set_diff_12}\n{set_diff_21}\n{set1_comp}\n{set2_comp}")

#Copying to clipboard for easier submition
pyperclip.copy(f"{set_union}\n{set_intersec}\n{set_diff_12}\n{set_diff_21}\n{set1_comp}\n{set2_comp}")