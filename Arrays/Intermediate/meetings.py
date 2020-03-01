
def merge_ranges(meetings):

    """

        This is a beautiful problem, that aims to identify the common meeting times of all the employees!

        Approach:
            1. What we first do is, we sort the given meeting timings according to the start time of the 
                meetings.
            2. Now, what we do is we check if the current meeting start time is less than the last meeting end time,
                if this is true, all we have to do is, append the start time of precious and then the max of the end times
                of the current and the precious one.
            3. If this is not the case, all we have to do is append the current tuple we have.


    """
    # This will sort the meetings according to the first element in each tuple.
    meetings = sorted(meetings)

    merged_meetings  = [meetings[0]]
    #This is another array, that we hhave and contains all the merged_meetings.

    for current_start,current_end in meetings:

        #If the current meeting start is less than or equal to the merged meeting ka end, we 
        #change the mmerged_meeting [-1] to the new values.
        if merged_meetings[-1][1] >= current_start:
            merged_meetings[-1] = (merged_meetings[-1][0],max(merged_meetings[-1][1],current_end))
        
        else:
            merged_meetings.append((current_start,current_end))
    
    return merged_meetings


meetings = [(5, 8), (1, 4), (6, 8)]
print(merge_ranges(meetings))