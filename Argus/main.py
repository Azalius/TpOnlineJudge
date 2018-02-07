import sys

def diff(a):
    return a.number


class Query:
    def __init__(self, number, time):
        self.number = number
        self.time = time
        self.nextTime = time

    def notif(self):
        self.nextTime += self.time
        print (self.number)

queries = []
for line in sys.stdin:
    words = line.strip().split()
    if words[0] == "#":
        break
    queries.append(Query(int(words[1]), int(words[2])))

i = 1
maxx = int(sys.stdin.readline().strip())
while i <= maxx:
    toDisplay = []
    minIntTime = int(sys.maxsize)
    for query in queries:
        if query.nextTime < minIntTime:
            minIntTime = query.nextTime
    for query in queries:
        if query.nextTime == minIntTime:
            toDisplay.append(query)

    toDisplay.sort(key=diff)
    for query in toDisplay:
        query.notif()
        i+=1
