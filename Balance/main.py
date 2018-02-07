import sys

def valide(stri):
    if stri == "":
        return True
    print(stri)
    if (stri[0] == "(" and stri[len(stri)-1] == ")") or (stri[0] == "[" and stri[len(stri)-1] == "]"):
         # print(stri + "striped from 1st & last : now " + stri[1:len(stri)-1])
        return valide(stri[1:len(stri)-1])
    index = 0
    while index <= len(stri) - 2:
        if stri[index] == ")" and stri[index+1] == "(":
            return valide(stri[index:]) and valide(stri[:index])
        if stri[index] == "]" and stri[index+1] == "[":
            return valide(stri[index:]) and valide(stri[:index])
        if stri[index] == ")" and stri[index+1] == "[":
            return valide(stri[index:]) and valide(stri[:index])
        if stri[index] == "]" and stri[index+1] == "(":
            return valide(stri[index:]) and valide(stri[:index])
        index += 1
    return False

nb = int(sys.stdin.readline().strip())
for i in range (0, nb):
    seq = sys.stdin.readline().strip()
    isValide = True
    if seq.count("(") != seq.count(")"):
        isValide = False
    if seq.count("[") != seq.count("]"):
        isValide = False
    if isValide:
        isValide = valide(seq)
    print(isValide)
