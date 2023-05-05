cows = {'Bessie' : [], 
        'Buttercup' : [], 
        'Belinda' : [], 
        'Beatrice' : [], 
        'Bella' : [], 
        'Blue' : [], 
        'Betsy' : [], 
        'Sue' : []}

constraints = []

with open("lineup.in", 'r') as input: 
    for i in range(int(input.readline())):
        constraints.append(input.readline().strip().split(" must be milked beside "))

for constraint in constraints:
    cows[constraint[0]].append(constraint[1])
    cows[constraint[1]].append(constraint[0])

order = []

def nextInChain(chain : list):
    neighborsOfEnd = cows[chain[-1]]
    if len(neighborsOfEnd) > 1:
        if chain[-2] != neighborsOfEnd[0]:
            return neighborsOfEnd[0]
        else:
            return neighborsOfEnd[1]
    else:
        if len(chain) > 1 and chain[-2] == neighborsOfEnd[0]:
            return None
        else:
            return neighborsOfEnd[0]


allCows = list(cows.keys())
allCows.sort()


for cow in allCows:
    if len(cows[cow]) > 2 or cow in order:
        continue
    elif len(cows[cow]) == 1:
            chain = [cow]
            next = nextInChain(chain)
            while next != None:
                chain.append(next)
                next = nextInChain(chain)
                
            for c in chain:
                if c in order:
                    order.remove(c)
            order += chain
    else:
        order.append(cow)


with open("lineup.out", 'w') as outFile:
    print("\n".join(order), file=outFile, end='')