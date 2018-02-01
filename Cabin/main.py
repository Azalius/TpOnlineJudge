import sys

nbLignes = int(sys.stdin.readline().strip())
nbLignesOk = 0

for i in range(0, nbLignes):
    val = []
    isOk = True
    lines = sys.stdin.readline().strip().split()
    for line in lines :
        val.append(float(line))
    if val[0] > 56.0 or val[1] > 45.0 or val[2] > 25.0:
        if val[0] + val[1] + val[2] > 125:
            isOk = False
    if val[3] > 7.0:
        isOk = False
    if isOk:
        print ("1")
        nbLignesOk +=1
    else:
        print("0")
print(nbLignesOk)
print("")
