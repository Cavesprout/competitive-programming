numWords, numDesc = input().split()

numWords = int(numWords)
numDesc = int(numDesc)

pointDict = {}

for i in range(numWords):
    word, points = input().split()
    pointDict[word] = int(points)


for j in range(numDesc):
    inLine = None
    salary = 0
    while inLine != ".":
        inLine = input()
        jobDesc = inLine.split()
        for word in jobDesc:
            if word in pointDict:
                salary += pointDict[word]
    print(salary)