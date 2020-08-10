#Importing libraries
library(readtext)
library(Biostrings)

#Setting working directory
setwd("D:/_Hector/R") 

#Reading sequence txt file
file = readtext(paste0(getwd(), "/rosalind_dna.txt"))
DNAsequence = DNAString(x = file$text[[1]])

#Transcribing sequence
RNAsequence = RNAString(x = DNAsequence)

#Printing accordingly
print(RNAsequence)