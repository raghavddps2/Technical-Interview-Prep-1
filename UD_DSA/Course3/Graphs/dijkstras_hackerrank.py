import sys
from collections import defaultdict

def printSolution(shortest_distance,start):
    ans = sorted(shortest_distance.items())
    for i in ans:
        if i[0] == start:
            continue
        elif i[1] >= 100000000000:
            print(-1,end=" ")
        else:
            print(i[1],end=" ")
    print()

def dijkstras(graph,start,nodes):

    shortest_distance = {}
    unseenNode = graph

    for i in range(1,nodes+1):
        shortest_distance[i] = sys.maxsize
    shortest_distance[start] = 0
    # print(shortest_distance)
    while unseenNode:

        minNode = None
        for i in unseenNode:
            # print(i,shortest_distance)
            if minNode is None:
                minNode = i
            elif(shortest_distance[i] < shortest_distance[minNode]):
                minNode = i
        
        for node,distance in unseenNode[minNode].items():
            for dis in distance:
                if shortest_distance[minNode]+dis < shortest_distance[node]:
                    shortest_distance[node] = shortest_distance[minNode]+dis
        unseenNode.pop(minNode)
    printSolution(shortest_distance,start)
    pass

t = int(input())
for _ in range(0,t):
    nodes,edges = map(int,input().split())
    graph = defaultdict(dict)

    for i in range(0,edges):
        start,end,weight = map(int,input().split())
        try:
            graph[start][end].append(weight)
            graph[end][start].append(weight)
        except:
            graph[start][end] = [weight]
            graph[end][start] = [weight]
    
    # print(graph)    
    start = int(input())
    dijkstras(graph,start,nodes)

#In this we cater to multiple roads within a city aas well!