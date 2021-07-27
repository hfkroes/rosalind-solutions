#Reading data from file
readData = File.open("rosalind_revc.txt")
dna_string = readData.read

#Complementing
complemented_string = ""

for i in 0..dna_string.length()
	base = dna_string[i]
	if (base != '')
		if (base == 'A')
			complemented_string = "T" + complemented_string
		elsif (base == 'T')
			complemented_string = "A" + complemented_string
		elsif (base == 'C')
			complemented_string = "G" + complemented_string
		elsif (base == 'G')
			complemented_string = "C" + complemented_string
		end
	end
end

#Printing results
print "#{complemented_string}"