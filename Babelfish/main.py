import sys

meaning = {}

for line in sys.stdin:
    words = line.strip().split()
    if not words:
        break
    meaning[words[0]] = words[1]

print (meaning)

for line in sys.stdin:
    word = []
    word = line.strip().split()
    if word[0] in meaning:
        print (meaning[word[0]])
    else:
        print ("eh")
