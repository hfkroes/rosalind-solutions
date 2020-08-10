#Importing libraries
library(readtext)
library(Biostrings)
library(clipr)

#Setting working directory
setwd("D:/_Hector/R") 

#Reading sequence txt file
file = readtext(paste0(getwd(), "/rosalind_rna.txt"))
DNAsequence = DNAString(x = file$text[[1]])

#Transcribing sequence
RNAsequence = RNAString(x = DNAsequence)

#Printing accordingly
print(RNAsequence)

#Copy to clipboard for easy submition
write_clip(as.character(RNAsequence))
