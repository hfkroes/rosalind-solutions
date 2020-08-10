#Importing libraries
library(readtext)

#Setting working directory
setwd("D:/_Hector/R") 

#Reading sequence txt file
file = readtext(paste0(getwd(), "/rosalind_fib.txt"))
variables = strsplit(file$text[[1]]," ")
n = as.integer(variables[[1]][1])
k = as.integer(variables[[1]][2])

#Defining function
rabbits <- function(n, k) {
  if(n == 1 || n == 2) {return (1)} else {return (rabbits(n-1, k)+(k*(rabbits(n-2, k))))}}

#Calculating rabbit number
rabbit_number = rabbits(n, k)

#Printing accordingly
print(rabbit_number)

#Copy to clipboard for easy submition
write_clip(as.character(rabbit_number))