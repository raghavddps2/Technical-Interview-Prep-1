import stack

st = stack.stack()
def area(hist_areas):
    areas = []
    for i in range(0,len(hist_areas)):
        # print("Items:\t",st.items)
        if st.is_empty() or hist_areas[i] > hist_areas[st.peek()]:
            st.push(i)
        
        else:
            # print(st.peek())
            while (not st.is_empty() and hist_areas[st.peek()] > hist_areas[i]):
                temp = st.pop()
                # print(temp)
                area = 0
                if st.is_empty():
                    area = hist_areas[temp]*i
                else:
                    area = hist_areas[temp]*(i-st.peek()-1)
                areas.append(area)   
            st.push(i) 
            # print("Areas:\t",areas)

    while(True):
        
        if st.is_empty():
            break
        else:
            temp = st.pop()
            area = 0
            if st.is_empty():
                area = hist_areas[temp]*len(hist_areas)
            else:
                area = hist_areas[temp]*(len(hist_areas)-st.peek()-1)
            areas.append(area)
            # print("Areas:\t",areas)
    return max(areas)

hist_areas = list(map(int,input().split()))
print("Max area is:\t",area(hist_areas))