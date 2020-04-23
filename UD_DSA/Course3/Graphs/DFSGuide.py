'''

    Adjacency matrix: 
        For each node, we basically have a n dimensional array telling with a 0 or a 1 if 
        an edge is there or not.

    Adjacency list:
        For each node, we have a list saying as to what all nodes it is connected to,
        In python, the appropriate data structure for an adjacency list can be a dictionary,
        where key represents the node and the value is a list of the connected nodes.
    
    Depth first search:

        1. Iterative Apprroach:

            In this approach, we simply use a stack to store the nodes in the order we visit them,
            ans we process try to process the next, next and next node and so on..
'''

def dfs_iterative(node_list):

    '''

        1. We maintain two arrays, one that can be used as a stack and other to determine 
        if we visited the node already.

        2. At the start, we will put the start of the graph into the stack.
        3. Then we will go through all the nodes connected to that node and put that in a stack.
        4. We even have a visited array so that we don't run into an infinite loop
            because graphs are connected.
    '''
    visited  = set()
    stack = []

    stack.append(0)

    print("DFS Traversal is coming")
    

    while len(stack) != 0:

        current_node = stack.pop(0)
        visited.add(current_node)
        print(current_node,end=" ")

        for node in node_list[current_node]:
            if node not in visited:
                stack.insert(0,node)
        # print(stack)
        
    print("\nDFS Traversal over")


def dfs_recursive(start_node,visited,node_list):

    #Printing the required node.
    print(start_node,end=" ")
    visited.append(start_node)
    connected_nodes = node_list[start_node]

    # Simple base case.
    if(connected_nodes == []):
        return

    #Traversing over the nodes further.
    for node in connected_nodes:
        if node not in visited:
            dfs_recursive(node,visited,node_list) 

dfs_iterative({0: [1, 2, 3], 1: [0], 2: [0, 4], 3: [0], 4: [2]})
visited = []
dfs_recursive(0,visited,{0: [1, 2, 3], 1: [0], 2: [0, 4], 3: [0], 4: [2]})
dfs_iterative({0: [1, 3], 1: [0, 2], 2: [1], 3: [0]})
visited = []
dfs_recursive(0,visited,{0: [1, 3], 1: [0, 2], 2: [1], 3: [0]})
dfs_iterative({0:[1,4,3,2],1:[0,5],2:[],3:[],4:[],5:[1,6],6:[]})
visited = []
dfs_recursive(0,visited,{0:[1,4,3,2],1:[0,5],2:[],3:[],4:[],5:[1,6],6:[]})