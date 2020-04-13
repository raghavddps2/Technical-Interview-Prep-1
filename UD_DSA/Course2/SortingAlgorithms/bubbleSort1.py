# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
    for i in range(0,len(l)-1):
        for j in range(len(l)-1,i+1,-1):
            if l[j][0] > l[j-1][0]:
                l[j],l[j-1] = l[j-1],l[j]
#     print(l)
    for i in range(0,len(l)-1):
        for j in range(len(l)-1,i,-1):
            if l[j][1] > l[j-1][1] and l[j][0] == l[j-1][0]:
                l[j],l[j-1] = l[j-1],l[j]
#     print(l)

#Smart Method.
def bubble_smart(l):
    for _ in range(0,len(l)):
        for index in range(1,len(l)):
            this_hour,this_min = l[index]
            prev_hour,prev_min = l[index-1]

            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue
            
            l[index] = (prev_hour,prev_min)
            l[index-1] = (this_hour,this_min)
bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")