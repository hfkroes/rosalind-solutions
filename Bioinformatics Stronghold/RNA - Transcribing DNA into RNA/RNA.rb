#Reading data from file
readData = File.open("rosalind_rna.txt")
dna_string = readData.read

for i in 0..dna_string.length()
	base = dna_string[i]
	if (base != '')
		if (base == 'T')
			print "U"
		else
			print base
		end
	end
end