'''

    Representation of graphs in Python is very easy. ALl we need is a dictionary

'''

graph = {
    "a":["c","b"],
    "b":["a"],
    "c":["a"]
}
edges = []
for node in graph:
    for neighbor in graph[node]:
        edges.append((node,neighbor))
print(edges)