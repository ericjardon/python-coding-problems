
def getScore(classStr):
    # Up to 10 of the words
    score = 0
    p = 10

    for level in classStr.split("-")[::-1]:
        if level == "upper":
            sublevel = 3
        elif level == "middle":
            sublevel = 2
        else: # lower
            sublevel = 1
        score += sublevel * (10**(p))
        p -= 1

    while p >= 0:
        # assume middle level of previous
        score += 2 * (10**(p))
        p -= 1

    return score

T = int(input()) # cases

for _ in range(T):
    n = int(input())
    table = {}

    for person in range(n):
        line = input().split()
        key = line[0][:-1]
        table[key] = getScore(line[1])
        
    sortedpeople = sorted(table.items(), key=lambda x: (-x[1], x[0]))
    for name, score in sortedpeople:
        print(name)
    print("==============================")


# print the names from highest to lowest class
