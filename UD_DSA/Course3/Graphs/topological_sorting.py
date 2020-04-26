from collections import defaultdict



def topological_sort(graph,nodes):

    indegree = {}
    for i in range(1,nodes+1):
        indegree[i] = 0

    for node in graph:
        node_connnects = graph[node]
        for i in node_connnects:
            indegree[i] += 1
            
    topological_sort_1 = []
    while indegree:
        ans = sorted(indegree.items(),key=lambda x: x[1])
        element = ans[0][0]
        topological_sort_1.append(element)
        del indegree[element]
        for node in graph[element]:
            indegree[node] -= 1
    return topological_sort_1

    
nodes,edges = map(int,input().split())
graph = defaultdict(set)
for i in range(0,edges):
    start,end = map(int,input().split())
    graph[start].add(end)
topological_sort(graph,nodes)
