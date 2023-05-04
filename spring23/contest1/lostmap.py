numVillages = int(input())

table = []

for line in range(numVillages):
    table.append(int(x) for x in input().split())

roads = set()

for i, line in enumerate(table):
    shortestVillageDist = (-1, 10000000)
    for j, dist in enumerate(line):
        if i == j:
            continue
        if dist < shortestVillageDist[1]:
            shortestVillageDist = (j, dist)
    roads.add((min(i,shortestVillageDist[0]),max(i,shortestVillageDist[0])))

for road in roads:
    print(road[0], road[1])