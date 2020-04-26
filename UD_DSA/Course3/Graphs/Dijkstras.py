import sys
graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'d':8,'b':4,'e':2},'d':{'e':7},'e':{'d':9}}

def dijkstras(graph,start,goal):

    shortest_distance = {}
    unseenNodes = graph
    predecessor  = {}
    path = []
    
    for i in unseenNodes:
        shortest_distance[i] = sys.maxsize
    shortest_distance[start] = 0

    while unseenNodes:

        minNode = None

        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for node,distance in unseenNodes[minNode].items():
            if shortest_distance[node] > shortest_distance[minNode]+distance:
                shortest_distance[node] = shortest_distance[minNode]+distance
                predecessor[node] = minNode
        unseenNodes.pop(minNode)
    print(shortest_distance)

    currentNode = goal

    while currentNode != start:
        path.insert(0,currentNode)
        currentNode = predecessor[currentNode]
    path.insert(0,start)

    print("Shortes distance to {} is {}".format(goal,shortest_distance[goal]))
    print("Path is: {}",str(path))

dijkstras(graph,'a','e')