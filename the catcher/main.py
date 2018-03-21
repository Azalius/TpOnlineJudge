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

def solve(arr):

arr=[]
for line in sys.stdin:
    nb = int(line.strip().split())
    if nb == -1:
        print ("maximum possible interceptions: "+ str(solve))
        arr = []
    else:
        arr.append(nb)
