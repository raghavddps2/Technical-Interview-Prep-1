wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):
    # TODO: Implement bubble sort solution
    for i in range(0,len(l)-1):
        for j in range(0,len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")