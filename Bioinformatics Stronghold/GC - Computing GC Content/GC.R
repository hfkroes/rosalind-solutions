#Importing libraries
library(Biostrings)

#Setting working directory
setwd("D:/_Hector/R") 

#Reading sequence multifasta file
strings = readDNAStringSet("rosalind_gc.txt", format="fasta",
                 nrec=-1L, skip=0L, seek.first.rec=FALSE,
                 use.names=TRUE, with.qualities=FALSE)

#Creating empty vector
GC_content_list <- vector(mode = "list", length = 2)

#Putting GC content and seq names in vector
for (seq_index in 1:length(strings)){
  seq_GC_content <- ((letterFrequency(strings[seq_index], letters="CG")[1]) / width(strings[seq_index]))
  GC_content_list[[1]][seq_index] = (names(strings))[seq_index]
  GC_content_list[[2]][seq_index] <- seq_GC_content[1]
}

#Organizing vector and turning it into data frame
names(GC_content_list) = c("names", "GC_content")
GC_content_df = as.data.frame(GC_content_list)

#Ordering elements by GC content
sorted_GC_list = GC_content_df[order(GC_content_df$GC_content, decreasing = TRUE),]

#Printing result name and GC content percentage
paste((head(sorted_GC_list, 1)$names), (((head(sorted_GC_list, 1)$GC_content))*100), sep = (" "))