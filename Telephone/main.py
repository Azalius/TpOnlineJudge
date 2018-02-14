import sys

class Interval:
    def __init__(self, start, duration):
        self.start = start
        self.duration = duration
        self.end = start + duration

    def activeDuring(self, interval):
        if self.start >= interval.end or self.end <= interval.start:
            return False
        return True



while True:
    words = sys.stdin.readline().strip().split()
    if words[0] == "0" and words[1] == "0":
        break
    N=int(words[0])
    M=int(words[1])
    i = 0
    calls = []
    while i < N:
        words = sys.stdin.readline().strip().split()
        calls.append(Interval(int(words[2]), int(words[3])))
        i +=1
    i=0
    while i < M:
        activeCalls = 0
        words = sys.stdin.readline().strip().split()
        inter = Interval(int(words[0]), int(words[1]))
        for call in calls:
            if call.activeDuring(inter):
                activeCalls+=1
        print (str(activeCalls))
        i+=1
