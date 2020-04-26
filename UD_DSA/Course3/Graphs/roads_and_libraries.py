from collections import defaultdict
queries = int(input())

def bfs(i,visited,graph,c):
    queue = [i]
    visited[i] = c
    while len(queue) > 0:
        node = queue.pop(0)
        for curr_node in graph[node]:
            if not visited[curr_node]:
                queue.append(curr_node)
                visited[curr_node] = c

for _ in range(0,queries):

    cities,roads,c_lib,c_road = map(int,input().split())
    graph = defaultdict(list)
    #This now completes the graph formation.
    for _ in range(roads):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0]*(cities+1)
    c  = 0
    for i in range(1,cities+1):
        if not visited[i]:
            c = c+1
            bfs(i,visited,graph,c)
    temp = defaultdict(int)
    for v in visited:
        temp[v] += 1
    t = c_lib*c
    for u,v in temp.items():
        t = t + (v-1)*c_road
    print(min(t,c_lib*cities))