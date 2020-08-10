#Importing libraries
library(readtext)
library(Biostrings)
library(clipr)

#Setting working directory
setwd("D:/_Hector/R") 

#Reading the sequence txt file
file = readtext(paste0(getwd(), "/rosalind_revc.txt"))
DNAsequence = DNAString(x = file$text[[1]])

#Reverse complementing the sequence
RevCompl = reverseComplement(DNAsequence)

#Printing accordingly
print(RevCompl)

#Copy to clipboard for easy submition
write_clip(as.character(RevCompl))
