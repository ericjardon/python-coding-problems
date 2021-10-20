'''
A queue of 1 to n persons
Any person can bribe (swap) with the person directly in front of them
Determine the _minimum_ number of swaps needed to get to a given queue order;
or if a person bribed more than twice, print 'Too chaotic'

CONSTRAINTS
1 <= t <= 10
1 <= n <= 10**5
'''

# A bribe from i implies that i moves 1 place forward.
# Any one element CANNOT be more than two places forward in the queue.

## WRONG APPROACH
def _minimumBribes(queue):
    N = len(queue)
    ans = 0
    temp = queue.copy()

    for i in range(N):
        bribes = queue[i] - (i+1)
        #print("Person", queue[i], "bribed", (bribes), "times")
    
        if bribes > 2:
            print("Too chaotic")
            return
        elif bribes > 0:
            temp.remove(queue[i])

        ans += max(bribes, 0)
    
    # Find who displaced later
    print("temp:", temp)
    i = 0
    while i < len(temp):
        j = i+1
        # If there are numbers ahead and are smaller than temp[i]
        while j < len(temp) and j <= i+2 and temp[i] > temp[j]:
            ans += 1
            j += 1
        i += 1
        
    print(ans)


def minimumBribes(q):
    pass





if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)