n,k = 5,3
rq,cq = 4,3
obstacles = [(5,5),(4,2),(2,3)]

def queensAttack(n,k,rq,cq,obstacles):

    all_possible_moves = []

    #All column moves.(column remain same)
    for i in range(1,n+1):
        if i != rq:
            all_possible_moves.append((i,cq))
    
    #All row moves. (row remains same)
    for i in range(1,(n+1)):
        if i != cq:
            all_possible_moves.append((rq,i))

    #Diagonal 1 (up side)
    for i in range(1,n-rq+1):
        all_possible_moves.append((rq+i,cq-i))
    
    #Diagonal 1 (down side)
    for i in range(1,n-cq+1):
        all_possible_moves.append((rq-i,cq+i))
    
    #Diagonal 2 (up side)
    for i in range(1,n-rq+1):
        all_possible_moves.append((rq+i,cq+i))
    
    #Diagonal 3 (down side)
    for i in range(1,n-cq+1):
        all_possible_moves.append((rq-i,cq-i))

    print(all_possible_moves)    
    all_possible_moves = set(all_possible_moves)
    #Till now, we got all the possible moves queen may take. 

    for i in obstacles:

        if i in all_possible_moves:

            #check if row point.
            if i[0] == rq:
                if i[1] < cq:
                    for i in range(1,i[1]+1):
                        all_possible_moves.remove((rq,i))
                else:
                    for i in range(i[1],n):
                        all_possible_moves.remove((rq,i))

            elif i[1] == cq:
                if i[0] < rq:
                    for i in range(1,i[0]+1):
                        all_possible_moves.remove((i,cq))
                else:
                    for i in range(i[0],n):
                        all_possible_moves.remove((i,cq))
 
            else:
                if i[0] < rq and i[1] < cq:
                    for j in range(0,min(rq,cq)):
                        if (i[0]-j,i[1]-j) in all_possible_moves:
                            all_possible_moves.remove((i[0]-j,i[1]-j))
                elif i[0] < rq and i[1] > cq:
                    for j in range(0,min(rq,cq)):
                        if (i[0]-j,i[1]-j) in all_possible_moves:
                            all_possible_moves.remove((i[0]-j,i[1]+j))
                elif i[0] > rq and i[1] < cq:
                    for j in range(0,min(rq,cq)):
                        if (i[0]-j,i[1]-j) in all_possible_moves:
                            all_possible_moves.remove((i[0]+j,i[1]-j))
                elif i[0] > rq and i[1] > cq:
                    for j in range(0,min(rq,cq)):
                        if (i[0]-j,i[1]-j) in all_possible_moves:
                            all_possible_moves.remove((i[0]+j,i[1]+j))
                else:
                    pass
        else:
            continue
    return len(all_possible_moves)

print(queensAttack(n,k,rq,cq,obstacles))