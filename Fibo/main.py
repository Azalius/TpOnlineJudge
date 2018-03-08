import sys

def fibonaci(n):
    if n <= 1:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)

termes = {}
termes[0] = 1
termes[1] = 1

def fibonaci2(n):
    if n in termes:
        return termes[n]
    ter = fibonaci2(n-1) + fibonaci2(n-2)
    termes[n] = ter
    return ter

def fibonaci3(n):
    m1 = 1
    m2 = 1
    res = 1
    for i in range(2, n):
        res = m2+m1
        m2 = m1
        m1 = res
    return res


for line in sys.stdin:
    words = line.strip().split()
    print(fibonaci3(int(words[0])))
