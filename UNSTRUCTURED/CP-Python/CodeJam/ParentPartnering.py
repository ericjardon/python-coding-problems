"""Scheduling problem: Two parents have to distribute activities between them
    in a way that no one person has to handle 2 overlapping activities.
    You are given the list of length N of starting and ending times Si,Ei,
    of each activity Ai. Return a string where the ith character is the person assigned
    to the ith activity, or return IMPOSSIBLE if no such schedule is possible.
    """
# We can use a priority queue of tasks according to start time
import heapq
def findSchedule(N: int) -> str:
    activities = list()     # list of N pairs: [Start, End]
    # read activities and push them to queue
    for _ in range(N):
        a = [int(x) for x in input().split(' ')]
        activities.append(a)
    heapq.heapify(activities)
    parents = [0, 0]    # the ith entry is the next available time for the ith person
    names = ["C", "J"]
    p = 0
    schedule = ""
    while (activities):
        si, ei = heapq.heappop(activities)      # pop next activity
        print("To dispatch:",si,ei)
        available = False
        # find next available parent and dispatch activity
        for _ in range(len(parents)):
            if parents[p] > si:     # if parent p is unavailable try next
                p = (p+1) % len(parents)     # next parent in list
            else:   # else we dispatch the activity
                print("Assigning to ", names[p])
                schedule += names[p]        # add parent's name to schedule
                parents[p] = ei     # set next available time of parent to ei
                available = True
                break
        if not available:
            return "IMPOSSIBLE"
    return schedule

def findSchedule2(N: int) -> str:
    activities = list()
    for _ in range(N):
        a = [int(x) for x in input().split(' ')]
        activities.append(a)
    heapq.heapify(activities)
    parents = [0, 0]
    names = ["C", "J"]
    schedule = ""
    while (activities):
        si, ei = heapq.heappop(activities)      # pop next activity
        print("To dispatch:",si,ei)
        available = False
        # traverse parents and pick the first available one
        for p in range(len(parents)):
            if parents[p] > si:     # unavailable, try next
                print(names[p], "unavailable")
                continue
            # Make the dispatch
            print("Assigning to ", names[p])
            schedule += names[p]
            parents[p] = ei
            available = True
            break
        if not available:
            return "IMPOSSIBLE"

    return schedule

for t in range(int(input())):   # input T
    result = findSchedule2(int(input()))
    print("Case # {}: {}".format(t+1, result))  # input N activities