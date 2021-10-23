## PRACTICE FIRST

def heights(A):
    # Basically we are asked for how many times we find a new local maximum
    max_height = 0
    rows = 0
    for i in range(len(A)):
        if A[i] >= max_height:
            rows += 1
            max_height = A[i]

    return rows

def distributeP(A):
    N = len(A)
    result = findMinDiff(A, 0, sum(A), N-1)
    return result


def findMinDiff(A, server1, server2, n, diff, memo = {}):
    # Can the processes be shared equally?
    if (server1, n) not in memo:
        if server1 == server2:
            return 0
        if server1 > server2:
            return min(server1-server2, diff)
        if n < 0:   # finished the array and server1 < server2 still
          return server2 - server1
        # Else, server2 > server1 so diff will be positive
        take = findMinDiff(A, server1 + A[n], server2 - A[n], n-1, server2-server1, memo)
        not_take = findMinDiff(A, server1, server2, n-1, server2-server1, memo)
        min_diff = min(take, not_take)
        memo[(server1, n)] = min_diff

    return memo[(server1, n)]

# we could also sort the processes by load and

def plusMinus(N, A):
    # A is an array of positions where '+' should appear.
    # You must return a string of same length as N where every other char is -
    # Note: strings are immutable
    ans = ""
    positions = set(A)
    for i in range(N):
        if i in positions:
            ans += "+"
        else:
            ans += "-"
    return ans


def minimumMysteryNum(S : str) -> str:
    answer = []
    # Comparing with previous, pick the minimum digit possible for each entry
    if len(S) == 1:
        if S == '?':
            return '1'
        return S

    def minDigit(i):
        if 0 < i < len(S)-1:
            prev = answer[i-1]
            nxt = S[i+1]
            if prev != '1' and nxt != '1':
                return '1'
            if prev == '2' or nxt == '2':
                return '3'
            return '2'

        elif i == 0:
            return str((S[i+1] == '1') + 1)         # first, only check next
        else:
            return str((answer[i-1] == '1') + 1)       # last, only check previous

    # Length is at least 2
    for i in range(len(S)):   # check all digits from 0 to previous-to-last
        if S[i] == '?':
            answer.append(minDigit(i))
            print(minDigit(i))
        else:
            answer.append(S[i])

    return ''.join(answer)



def main():
    print(minimumMysteryNum('?132?2??1?'))

main()
import sys
sys.stderr.write(
    ''
)