#Importing libraries
import pyperclip, itertools

#Reading variables txt file
file = open('rosalind_ba3h.txt', 'r')
input_file = file.read().split('\n')

k = int(input_file[0]); reads = [input_file[a] for a in range(1, len(input_file))]

#Defining functions
def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1

import itertools

def make_dictionary(reads, k):
    n = 1
    prefixes = {}
    count = len(reads)
    todel = []
    for a in range(count):
        prefixes[reads[a]] = reads[a][0:k]
    olens = {} 
    for elem in range(count):
        suffix = reads[elem]
        for pref in range(count):
            preffix = prefixes[reads[pref]]
            if pref != elem:
                over = 0
                find = suffix.find(preffix)
                preffix = reads[pref]
                if find != -1:
                    over = overlap(suffix, preffix, k)
                if over >= k:
                    ituple = suffix, preffix
                    olens[ituple] = over
    print('Dictionary created successfully!')
    return olens, reads, prefixes, n

def renovate_dictionary(reads, dictionary, prefixes, read_a, read_b, read_c, k, n):
    topop = []
    for x in list(dictionary)[0:len(dictionary)]:
        a = ("{}, {} ".format(x,  dictionary[x])).split()
        reada = a[0].replace("('", '').replace("',", '')
        readb = a[1].replace("'),", '').replace("'", '')
        if reada == read_a or reada == read_b or readb == read_a or readb == readb:
            topop.append(x)
    for pop in topop:
        dictionary.pop(pop)
    suffix = read_c
    for pref in range(len(reads)):
        index = reads[pref]
        preffix = prefixes[index]
        over = 0
        find = suffix.find(preffix)
        preffix = reads[pref]
        if preffix != suffix:
            if find != -1:
                over = overlap(suffix, preffix, k)
            if over >= k:
                ituple = suffix, preffix
                dictionary[ituple] = over
    for elem in range(len(reads)):
        preffix = prefixes[read_c]
        suffix = reads[elem]
        over = 0
        find = suffix.find(preffix)
        preffix = read_c
        if preffix != suffix:
            if find != -1:
                over = overlap(suffix, preffix, k)
            if over >= k:
                ituple = suffix, preffix
                dictionary[ituple] = over
    print('Assembly', n, 'processed successfully!')
    n += 1
    return dictionary, n

def greedy_scs(reads, k):
    dictionary = {}
    dictionary, reads, prefixes, n = make_dictionary(reads, k)
    while len(reads) > 1:
        dictionary = {key: value for key, value in sorted(dictionary.items(), reverse = True, key=lambda item: item[1])}
        for x in list(dictionary)[0:1]:
            a = ("{}, {} ".format(x,  dictionary[x])).split()
            read_a = a[0].replace("('", '').replace("',", '')
            read_b = a[1].replace("'),", '').replace("'", '')
            olen = int(a[2])
        reads.remove(read_a)
        reads.remove(read_b)
        read_c = read_a + read_b[olen:]
        prefixes[read_c] = read_c[0:k]
        reads.append(read_c)
        dictionary, n = renovate_dictionary(reads, dictionary, prefixes, read_a, read_b, read_c, k, n)
    return ''.join(reads)

#Creating string
gscs = greedy_scs(reads, k-1)

#Printing string
print(f"\nResulting string:\n{gscs}")

#Copying to clipboard for easier submition
pyperclip.copy(gscs)