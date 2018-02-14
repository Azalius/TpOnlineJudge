import sys

def isprime(n):
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True



while True:
    words = int(sys.stdin.readline().strip().split()[0])
    if words == "0":
        break
    i = 3
    found = False
    while i < words:
        if isprime(i):
            j = int(words / 2.0) - 1
            while j < words :
                if isprime(j):
                    if i + j == words:
                        if found == False:
                            found = True
                            n1 = i
                            n2 = j
                        else:
                            if n2-n1 < j-i:
                                n1 = i
                                n2 = j
                j+=2
        i+=2
    if not found:
        print("Conjecture fausse pour "+ str(words))
    else:
        print(str(words) + " = " + str(n1) + " + " + str(n2))
