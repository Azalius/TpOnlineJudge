import sys

meaning = {}

for line in sys.stdin:
    words = line.strip().split()
    if not words:
        break
    meaning[words[0]] = words[1]


for line in sys.stdin:
    word = []
    word = line.strip().split()
    ok = False
    for k, v in meaning.items():
        if v == word[0]:
            print(k)
            ok = True
            break
            # print (k + " diif from " + word[0])
    if not ok:
        print ("eh")
