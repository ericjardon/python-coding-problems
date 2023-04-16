"""
HackerRank problem seen in C3 screening assessment

There are n students numbere 1 to n.
Given three different arrays of same length:
- queryType: either "Friend" or "Total"
- students: a pair of students (i,j), where 1<=i,j<=n

"Friend" query indicates sutenst i and j become friends
"Total" query indicates the sum of the groups of friends of both students i and j

Return an array of integers where each integer is the answer to each "Total" query in order
"""

# Re-worked solution. Could not deliver all test cases in time; unresolved debugging issues.

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, i, j):
    pi = find(parent, i)
    parent[j] = pi

def areFriends(parent, i, j):
    return find(parent, i) == find(parent, j)

def getTheGroups(n, queryType, students):
    
    parent = [i for i in range(n+1)]
    ans = []

    for q, args in zip(queryType, students):
        i, j = args
        if q == "Friend":
            if not areFriends(parent, args[0], args[1]):
                print("Friend", i, j)
                union(parent, i, j)
                print(parent)
            else:
                print(i, j, f"Already friends (parent {find(parent,i)})")
        
        elif q == "Total":
            print("get friend count", i, j, end=": ")
            tot = getFriendsCount(parent, i, j, n)
            print(tot)
            ans.append(tot)

    return ans

def getFriendsCount(parent, i, j, n):
    g1 = find(parent, i)
    g2 = find(parent, j)

    friendGroups = {g1, g2}

    return sum(
        1
        for k in range(1, n+1)      # for every student 1...n
        if find(parent, k) in friendGroups
    )

if __name__ == "__main__":
    queryType = ["Friend", "Total", "Friend", "Total", "Friend", "Total", "Friend", "Total", "Friend", "Friend", "Total"]
    students = [[1, 2], [1,5], [2, 3], [1,5], [3, 4], [1,5], [5, 7], [1,5], [7, 6], [4, 5], [1,5]]
    getTheGroups(7, queryType, students)