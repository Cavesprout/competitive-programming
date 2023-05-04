def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

# graph = {
#     "W" : ["X", "Y"],
#     "X" : ["W", "Z", "Y"],
#     "Y" : ["W", "X", "Z"],
#     "Z" : ["X", "Y"]
# }
# graph = { 1: [2, 3, 5], 2: [1], 3: [1], 4: [2], 5: [2] }
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B"],
    "D": ["A", "B"]
}
cycles = [[node]+path  for node in graph for path in dfs(graph, node, node)]
print(len(cycles))
print(cycles)