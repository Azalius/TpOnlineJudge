import sys

oldLine = None
Matrix = None

def PLS(c1, c2):
    if len(c1) == 0 or len(c2) == 0:
        return 0
    if Matrix[len(c1)][len(c2)] != -1:
        return Matrix[len(c1)][len(c2)]

    if c1[-1:] == c2[-1:]:
        Matrix[len(c1)][len(c2)] = PLS(c1[:-1], c2[:-1]) + 1
        return PLS(c1[:-1], c2[:-1]) + 1
    else:
        v1 = PLS(c1[:-1], c2[:-1])
        v2 = PLS(c1[:-1], c2)
        v3 = PLS(c1, c2[:-1])
        if v1>= v2 and v1 >= v3:
            Matrix[len(c1)][len(c2)] = v1
            return v1
        if v2 >= v3 and v2 >= v1:
            Matrix[len(c1)][len(c2)] = v2
            return v2
        Matrix[len(c1)][len(c2)] = v3
        return v3


for line in sys.stdin:
    words = line.strip().split()
    if oldLine == None:
        oldLine = words[0]
    else:
        Matrix = [[-1 for x in range(len(oldLine) + 1)] for y in range(len(words[0])+1)]
        print(PLS(oldLine, words[0]))
        Matrix = None
        oldLine = None
