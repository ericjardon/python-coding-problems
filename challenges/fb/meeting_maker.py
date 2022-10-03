# Youre given a 2d array of pairs (start, end) that represent meetings in a day.
# schedule[i][j] represents the jth meeting in the day for the ith coworker.

# Given a meeting length k, find the earliest time available for all coworkers to meet.
# If none is available, return -1


## FIRST APPROACH: compute based on busy times
# FIRST: make a schedule of aggregated meetings. This involves finding the union of closed intervals
# SECOND: find the first time t such that t+length = next_busy_time
# THIRD: return -1 if such t is not found

def intersect1(meet1, meet2):
    return (meet1[0] <= meet2[0] <= meet1[1]) or (meet2[0] <= meet1[0] <= meet2[1])

def nextMeeting(sch1, sch2, i, j):
    # Returns next meeting's starting time and end time.
    # as well as a flag to indicate i or j
    meet_i = sch1[i] if i < len(sch1) else None
    meet_j = sch2[j] if j < len(sch2) else None

    if meet_i and meet_j:
        return (meet_i, True) if meet_i[0] < meet_j[0] else (meet_j, False)
    
    if meet_i:
        return (meet_i, True)
    if meet_j:
        return (meet_j, False)
    
    return None


def mergeMeetings(sch1, sch2):

    if not sch1:
        return sch2
    if not sch2:
        return sch1
    busy = []

    # pick the earliest start. while next start is less than current end,  append.

    starti, endi = sch1[0]
    startj, endj = sch2[0]

    earliest_start = None
    latest_end = None
    i = 0 # next interval in sch1
    j = 0 # next interval in sch2

    if starti < startj:
        earliest_start, latest_end = starti, endi
        i += 1
        pass
    else:
        earliest_start, latest_end = startj, endj
        j += 1
    
    while True:
        # merge as long as next overlaps
        next_meeting, next_is_i = nextMeeting(sch1, sch2, i, j)

        while next_meeting and next_meeting[0] < latest_end:
            # next meeting starts before current ends => overlap
            # extend to next[end]
            latest_end = next_meeting[1]
            if next_is_i:
                i += 1
            else:
                j += 1
            next_meeting = nextMeeting(sch1, sch2, i, j)

        print('min start', earliest_start)
        print('max end', latest_end)
        busy.append([earliest_start, latest_end])

        if next_meeting is None:
            break
        # No more overlap, so simply set next start and end to next_meeting
        earliest_start, latest_end = next_meeting
    

## TO BE CONTINUED
    
    

