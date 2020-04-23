def countNodes(start,node_list,visited,count):

    visited.append(start)
    count[0] = count[0] + 1

    if len(node_list[start]) == 0:
        return
    
    for city in node_list[start]:
        if city not in visited:
            countNodes(city,node_list,visited,count) 

def getAns(start,node_list,visited,count,c_lib,c_road):
    cost = 0
    for i in node_list.keys():
        if i not in visited:
            countNodes(i,node_list,visited,count)
            if c_lib > c_road:
                cost = cost + c_lib + (count[0]-1)*c_road
            else:
                cost = cost + c_lib*count[0]
            count[0] = 0
    return cost


visited = []
a = [0]
print(getAns(1,{1: [3, 2], 3: [1, 4, 2], 4: [3, 2], 2: [4, 1, 3], 5: [6], 6: [5]},visited,a,2,5))
