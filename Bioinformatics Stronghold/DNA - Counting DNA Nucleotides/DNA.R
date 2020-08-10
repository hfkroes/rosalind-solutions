#Importing libraries
library(readtext)
library(Biostrings)

#Setting working directory
setwd("D:/_Hector/R") 

#Reading sequence txt file
file = readtext(paste0(getwd(), "/rosalind_dna.txt"))
sequence = DNAString(x = file$text[[1]])

#Calculating frequencies
freq_matrix = alphabetFrequency(sequence)

#Printing accordingly
print(freq_matrix[1:4])