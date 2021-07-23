#Reading data from file
readData = File.open("rosalind_dna.txt")
dna_string = readData.read

#Counting
a_count=0
t_count=0
c_count=0
g_count=0

for i in 0..dna_string.length()
	base = dna_string[i]
	if (base != '')
		if (base == 'A')
			a_count += 1
		elsif (base == 'T')
			t_count += 1
		elsif (base == 'C')
			c_count += 1
		elsif (base == 'G')
			g_count += 1
		end
	end
end

#Printing results
print "#{a_count} #{c_count} #{g_count} #{t_count}"