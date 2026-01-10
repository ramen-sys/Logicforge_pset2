def min_cancelled_bookings(intervals):
    if not intervals:
        return None
    else:
        intervals.sort(key=lambda x:x[1])

        prev=intervals[0][1]
        min_rem=0
        for slot in intervals[1:]:

            if slot[0]>=prev:
                prev=slot[1]
            else:
                interval=intervals.remove(slot)
                min_rem+=1


    return min_rem
print(min_cancelled_bookings( [[1, 2], [5, 10], [18, 35]]))