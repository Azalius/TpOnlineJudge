import sys
array = []

def fill(arraye):
    maxe = 0
    cour = 0
    for nb in arraye:
        cour = max(cour, 0)
        cour += nb
        maxe = max(cour, maxe)
    return maxe

def solve(arraye):
    maxSum = fill(arraye)
    if maxSum > 0:
        return 'The maximum winning streak is ' + str(maxSum) +'.'
    else:
        return 'Losing streak.'

restant = 0
while True:
    Nbs = sys.stdin.readline().strip().split()
    for N in Nbs:
        if int(N) == 0:
            break
        if restant == 0 and len(array) != 0:
            print(array)
            print(solve(array))
        elif restant == 0:
            restant = int(N)
            array = []
        else:
            restant -= 1
            array.append(int(N))
