import math

with open("moocast.in", 'r') as input: 
    numCows = int(input.readline().strip())
    cows = []
    for i in range(numCows):
        line = input.readline().strip().split(" ")
        # CowNum, x, y, power
        cows.append((i, int(line[0]), int(line[1]), int(line[2])))

# Sort by x coordinate
cows.sort(key = lambda x : x[1])

cowNeighbors = []

def checkInRange(x1, y1, p, x2, y2):
    # Try two diff distance metrics
    # if abs(x1-x2) <= p and abs(y1-y2) <= p: 
    if abs(math.dist((x1, y1), (x2, y2)))-1 <= p:
        return True
    else:
        return False
    
# Build graph of cows
for i in range(numCows):
    neighbors = []
    cow = cows[i]
    checkCowNum = i - 1
    while (checkCowNum >= 0 and cows[checkCowNum][1] > cow[1] - cow[3]):
        cowInRange = checkInRange(cow[1], cow[2], cow[3], cows[checkCowNum][1], cows[checkCowNum][2])
        if cowInRange:
            neighbors.append(cows[checkCowNum][0])
        checkCowNum -= 1
            
    checkCowNum = i + 1
    while (checkCowNum < numCows and cows[checkCowNum][1] < cow[1] + cow[3]):
        cowInRange = checkInRange(cow[1], cow[2], cow[3], cows[checkCowNum][1], cows[checkCowNum][2])
        if cowInRange:
            neighbors.append(cows[checkCowNum][0])
        checkCowNum += 1
    
    cowNeighbors.append(neighbors)

# Found cow with greatest nested connections

def getAllConnected(cowNum, visited):
    newVisited = visited.copy()
    for connectedCow in cowNeighbors[cowNum]:
        if connectedCow not in visited:
            newVisited.add(connectedCow)
            newVisited.union(getAllConnected(connectedCow, newVisited))
    
    return newVisited

biggestReach = set()

for cow in range(numCows):
    # Can always reach itself
    canReach = getAllConnected(cow, set([cow]))
    if len(biggestReach) < len(canReach):
        biggestReach = canReach


print(cowNeighbors)

with open("moocast.out", 'w') as outFile:
    print(len(biggestReach), file=outFile, end='')


# Once again I feel like I overcomplicated this one, but I got there. I ended up naming my variables
# in a way that made it confusing to discern them once things got more complicated, need to make sure
# I stop naming everything some variation on "cows" "num" and "cowsNum".