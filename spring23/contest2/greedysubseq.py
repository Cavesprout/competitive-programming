seqLen = input()
seq = input().split()

seqInt = []

for i in seq:
    seqInt = int(i)


greedyResults = []

while len(seq) > 0:
    newResult = []
    testSet = seq.copy()
    for i, item in enumerate(testSet):
        if len(newResult) > 0:
            if (item > newResult[-1]):
                seq.remove(item)
                newResult.append(item)
        else:
            seq.remove(item)
            newResult.append(item)
    
    greedyResults.append(newResult)

print(len(greedyResults))
for res in greedyResults:
    for x in res:
        print(x, end=" ")
    print("")

# Ran out of time so I cannot test my solutions but it works with the example problem so I consider it a win