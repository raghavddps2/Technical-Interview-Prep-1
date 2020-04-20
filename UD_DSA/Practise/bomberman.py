from queue import Queue
def generalizedBomberman(n,grid):
    # print("*********ANS***********")
    q = Queue()
    for i in range(0,len(grid)):
        grid[i] = list(grid[i])
    if n == 1:
        return grid
    bombs1 = []
    for row in range(0,len(grid)):
        for col in range(0,len(grid[row])):
            if grid[row][col] == 'O':
                bombs1.append((row,col))
    time = 2
    q.put(bombs1)
    while time <=n:
        # print(q.queue)
        if time%2 == 0:
            for row in range(0,len(grid)):
                for col in range(0,len(grid[row])):
                    grid[row][col] = 'O'
        else:
            a = q.get()
            print(a)
            print(grid)
            for i in a:
                grid[i[0]][i[1]] = '.'
                if (i[0]-1) >= 0:
                    grid[i[0]-1][i[1]] = '.'
                if (i[0]+1) < len(grid):
                    grid[i[0]+1][i[1]] = '.'
                if (i[1]-1) >= 0:
                    grid[i[0]][i[1]-1] = '.'
                if (i[1]+1) < len(grid[0]):
                    grid[i[0]][i[1]+1] = '.'
            bombs = []
            for row in range(0,len(grid)):
                for col in range(0,len(grid[row])):
                    if grid[row][col] == 'O':
                        bombs.append((row,col))
            q.put(bombs)
        time = time + 1
    for i in range(0,len(grid)):
        [print(j,end="") for j in grid[i] ]
        print()

rows,columns,time = map(int,input().split())
grid = []
for i in range(0,rows):
    grid.append(input())
generalizedBomberman(time,grid)

