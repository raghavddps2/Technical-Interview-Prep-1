def minTime(machines, goal):

    i = 1
    while(True):
        if (sum(i // j for j in machines) == goal):
            print(i)
            break
        i = i +1
        # print("hi")

machines = [2,3,2]
goal = 10
minTime(machines,goal)