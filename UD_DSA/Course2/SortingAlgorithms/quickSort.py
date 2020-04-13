'''

    We are talking about quick sort now!
    This is a beautiful algorithm, all we have to do is to select a pivot value,
    
    1. Select last element as the pivot.
    2. All element less than pivot are placed to left
    3. All element greater than the pivot are placed to the right
    4. Once we are done with this step, all we do is to iterate on the left and right half of the array.

'''
def get_pivot(items,start_index,end_index):

    pivot_index = end_index
    pivot_value = items[pivot_index]

    while start_index != pivot_index:
        item = items[start_index]
        if item <= pivot_value:
            start_index = start_index + 1
            continue
        
        #else, we should go ahead with this.
        items[start_index] = items[pivot_index-1]
        items[pivot_index-1] = pivot_value
        items[pivot_index] = item
        pivot_index = pivot_index -1 
    return pivot_index

def quick_sort(items,start_index,end_index):

    if end_index <= start_index:
        return
    pivot = get_pivot(items,start_index,end_index)
    quick_sort(items,start_index,pivot-1)
    quick_sort(items,pivot+1,end_index)

a = [6,5,4,3,2,1]
quick_sort(a,0,len(a)-1)
print(a)