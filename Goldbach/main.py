import sys
from math import sqrt

def primes(n):
        tableau = [False, False] + [True]*(n-2)
        tableau[2::2] = [False]*((n-2)//2 + n%2) # supr. des nb pairs
        yield 2 # 2 est un nombre premier
        racine = int(n**0.5)
        racine = racine + [1,0][racine%2] # pour que racine soit impair
        i, fin, pas = 3, racine+1, 2
        while i<fin: # on ne traite que les nb impairs
            if tableau[i]:
                yield i # i est un nombre premier
                # on élimine i et ses multiples
                tableau[i::i] = [False]*((n-i)//i + int((n-i)%i>0))
            i += pas
        i, fin, pas = racine, n, 2
        while i<fin:  # on ne traite que les nb impairs
            if tableau[i]:
                yield i # i est un nombre premier
            i += pas

premiers = []
for pr in primes(1000000):
    premiers.append(pr)

print(premiers)

while True:
    words = int(sys.stdin.readline().strip().split()[0])
    if words == "0":
        break
    found = False
    for i in premiers:
        for j in premiers:
            if i + j == words:
                if found == False:
                    found = True
                    n1 = i
                    n2 = j
                else:
                    if n2-n1 < j-i:
                        n1 = i
                        n2 = j
    if not found:
        print("Conjecture fausse pour "+ str(words))
    else:
        print(str(words) + " = " + str(n1) + " + " + str(n2))
