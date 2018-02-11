import sys

equipes = {}
tocards = []
alreadyreg = []
equipe = ""

def taille(equipe):
    nb = 0
    for pers in equipe:
        if pers not in tocards:
            nb += 1
    return nb

def displayEquipe():
    while equipes:
        sameNumberEquipes = []
        nb = 0
        for equi, pers in equipes.items():
            nbper = taille(pers)
            if nbper > nb:
                nb = nbper
        for equi, pers in equipes.items():
            nbper = taille(pers)
            if nb == nbper:
                sameNumberEquipes.append(equi)

        sameNumberEquipes.sort()
        for equipe in sameNumberEquipes:
            print(equipe + " " + str(nb))
            del equipes[equipe]


for line in sys.stdin:
    words = line.strip()
    if words == "0":
        break
    elif words == "1":
        displayEquipe()
        equipes = {}
        tocards = []
        alreadyreg = []
    elif words.capitalize()[0] == words[0]:
        if equipe in equipes.keys():
            for pers in equipes[equipe]:
                alreadyreg.append(pers)
        equipe = words
        equipes[words] = []
    else:
        if words in alreadyreg:
            tocards.append(words)
        elif words not in equipes[equipe]:
            if words not in alreadyreg:
                equipes[equipe].append(words)
