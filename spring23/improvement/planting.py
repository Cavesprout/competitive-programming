

# Create Graph of field Neighbors
with open("planting.in", 'r') as input: 
    fieldNeighbors = {}
    fieldTypes = []
    numFields = int(input.readline())
    for i in range(numFields):
        fieldNeighbors[i+1] = []
        fieldTypes.append(0)
    for i in range(numFields - 1):
        path = input.readline().strip().split(" ")
        fieldNeighbors[int(path[0])].append(int(path[1]))
        fieldNeighbors[int(path[1])].append(int(path[0]))

# Rules:
# The same grass type cannot be in two adjacent fields
# The same grass type cannot be in two fields with only one field between them

maxNumTypes = 0

# Strategy: For each node, determine the number of nodes that cannot be the same type of grass.
# Update the number of types of grass to always be the maximum number found.

for field in fieldNeighbors.keys():
    # Number of distinct grass types must be 1 + number of neighbors
    numTypes = len(fieldNeighbors[field]) + 1
    maxNumTypes = max(maxNumTypes, numTypes)


with open("planting.out", 'w') as outFile:
    print(maxNumTypes, file=outFile, end='')

# I tried to make this problem far more difficult for myself than it needed to be. After stopping for a moment I realized that
# I just needed to find the most restricted point in the graph and I would have my solution. Will definitely need a harder one.