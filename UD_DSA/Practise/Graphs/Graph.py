class Graph(object):

    def __init__(self):
        self.graph = {}
    
    def addVertex(self,vertex):
        if vertex in self.graph:
            return
        else:
            self.graph[vertex] = []

    def addEdge(self,edge):
        vertex1,vertex2 = edge
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
    
    def printVertices(self):
        for i in self.graph:
            print(i,end=" ")

    def printEdges(self):
        for node in self.graph:
            for neighbor in self.graph[node]:
                print((node,neighbor),end=" ")

    def __str__(self):
        print("Vertcies are")
        self.printVertices()
        print("\nEdges are: ")
        self.printEdges()
        return ""

G = Graph()
G.addVertex("a")
G.addVertex("b")
G.addVertex("c")
G.addVertex("d")
G.addVertex("e")
G.addEdge(("a","b"))
G.addEdge(("a","e"))
G.addEdge(("b","c"))
G.addEdge(("c","d"))
print(G)