import sys

def valide(stri):
    index = 0
    cars = []
    while index <= len(stri) -1:
        if stri[index] == "(" or stri[index] == "[":
            cars.append(stri[index])
        elif not cars:
            return False
        if stri[index] == ")":
            if cars.pop() != "(":
                return False
        if stri[index] == "]":
            if cars.pop() != "[":
                return False
        index+=1
    return not cars

nb = int(sys.stdin.readline().strip())
for i in range (0, nb):
    if valide(sys.stdin.readline().strip()):
        print("Yes")
    else:
        print("No")
