import sys
for line in sys.stdin:
    numbers = []
    isJolly = True
    words = line.strip().split()
    for word in words:
        numbers.append(int(word))
    diffRef = abs(numbers[0] - numbers[1])
    index = 0
    while index <= len(numbers) - 2:
        if abs(numbers[index] - numbers[index + 1]) is not diffRef - index:
            isJolly = False
        index += 1
    if isJolly:
        print("Jolly")
    else :
        print("Not Jolly")

print(numbers)
