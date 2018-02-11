import sys

for line in sys.stdin:
    i = 0
    words = line.strip().upper()
    while i < len(words)-1:
        if words[i] == "A" or words[i] == "B" or words[i] == "C":
            print("2")
        elif words[i] == "D" or words[i] == "E" or words[i] == "F":
            print("3")
        elif words[i] == "G" or words[i] == "H" or words[i] == "I":
            print("4")
        elif words[i] == "J" or words[i] == "K" or words[i] == "L":
            print("5")
        elif words[i] == "M" or words[i] == "N" or words[i] == "O":
            print("6")
        elif words[i] == "P" or words[i] == "Q" or words[i] == "R" or words[i] == "S":
            print("7")
        elif words[i] == "T" or words[i] == "U" or words[i] == "V":
            print("8")
        elif words[i] == "W" or words[i] == "X" or words[i] == "Y" or words[i] == "Z":
            print("9")
        else:
            print(words[i])
        i += 1
