#Importing libraries
import pyperclip

#Reading variables txt file
file = open('rosalind_lgis.txt', 'r')
n, pi = file.read().split('\n')
n = int(n); pi = list(map(int, pi.split()));

#Defining functions
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = [a[x-1]] + result
            x -= 1
            y -= 1
    return result

def problem(n, pi):
    incr = lcs(pi, sorted(pi))
    decr = lcs(pi, sorted(pi, reverse=True))
    return (incr, decr)

#Calculating sequence
incr, decr = problem(n, pi)

#Printing result
print(f"{' '.join(str(i) for i in incr)}\n{' '.join(str(i) for i in decr)}")

#Copying to clipboard for easier submition
pyperclip.copy(f"{' '.join(str(i) for i in incr)}\n{' '.join(str(i) for i in decr)}")