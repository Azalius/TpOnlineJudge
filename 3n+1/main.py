import sys

niv = {}

def length(i):
    if i == 1:
        return 1
    if i in niv:
        return niv[i]
    if i%2 == 0:
        res = 1 + length(i/2)
    else:
        res = 1 + length(3*i+1)
    niv[i] = res
    return res

def solve(i, j):
    maxe = 1
    for a in range(min(i, j), max(i, j)+1):
        maxe = max(length(a), maxe)
    return str(maxe)

for line in sys.stdin:
    words = line.strip().split()
    print(words[0] + " " + words[1]+" "+ solve(int(words[0]), int(words[1])))
