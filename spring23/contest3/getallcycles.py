# Pick a point, move to all neighboring points until we get back to 
# starting point


# Variables
# Lists
# Dictionaries
# Functions
# Function Parameters
# Recursion - A function calls itself.
# Classes

# Key: A named vertex
# Values: All neighboring vertices
Graph = {
    "W" : ["X", "Y"],
    "X" : ["W", "Z", "Y"],
    "Y" : ["W", "X", "Z"],
    "Z" : ["X", "Y"]
}

# startPoint = Where we started, and where we're looking to go
# currentPoint = Where we are in the graph traversal
# pathSoFar = A list of all the points we've seen in order
# completePathsFound = A list of all complete paths we've found
def FindCycles(startPoint, currentPoint, pathSoFar, completePathsFound):
    neighbors = Graph[currentPoint]
    pathSoFar.append(currentPoint)
    for vertex in neighbors:
        if vertex == pathSoFar[-1]:
            return completePathsFound
        elif vertex in pathSoFar:
            if vertex == startPoint:
                # If our neighbor is our start point (but not the previous point)
                # Then we found a complete cycle!
                # return it to the top of the program.
                completePathsFound.append(pathSoFar)
                return completePathsFound
        else:
            completePathsFound += FindCycles(startPoint, vertex, pathSoFar, completePathsFound)


# Run the program
visited = []
AllCompleteCycles = []
for start in Graph:
    nextSearch = visited.copy()
    nextSearch.append(start)
    AllCompleteCycles += FindCycles(start, start, nextSearch, [])