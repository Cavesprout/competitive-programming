numRuns = int(input())

numA = 1
numB = 0

nextA = 1
nextB = 0

for i, count in enumerate(range(numRuns)):
    nextA = numB
    nextB = numA + numB

    numA = nextA
    numB = nextB

print(numA, numB)