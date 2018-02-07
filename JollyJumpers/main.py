import sys
for line in sys.stdin:
    numbers = []
    difs = []
    isJolly = True
    words = line.strip().split()
    for word in words:
        numbers.append(int(word))
    index = 1
    while index <= len(numbers) - 2:
        difs.append(abs(numbers[index] - numbers[index + 1]))
        index += 1
    index = 1
    while index <= len(difs):
        if not index in difs:
            isJolly = False
        index += 1
    if isJolly or len(numbers) == 1:
        print("Jolly")
    else :
        print("Not jolly")
