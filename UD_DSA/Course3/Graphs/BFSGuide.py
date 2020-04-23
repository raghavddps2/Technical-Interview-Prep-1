from queue import Queue
def breadth_first_search(node_list):

    '''

        1. First concept in breadth first search is that, we finish all the nodes connected to a vertex.
        2. This simply tells that we plan to use a queue data structure
    '''

    queue = []
    queue.append(0)
    visited = []
    visited.append(0)
    while len(queue) > 0:
        get_node = queue.pop(0)
        print(get_node,end=" ")
        for node in node_list[get_node]:
            if node not in visited:
                queue.append(node)
                visited.append(get_node)
    return

breadth_first_search({0: [1, 2, 3], 1: [0], 2: [0, 4], 3: [0], 4: [2]})
print()
breadth_first_search({0:[1,4,3,2],1:[0,5],2:[],3:[],4:[],5:[1,6],6:[]})
