"""Given the history of activities by a given user,
 calculate the max number of months he can last
 while redeeming as less laddus as possible each month."""

def main():
    try:
        T = int(input())
        for _ in range(T):
            head = input().split(" ")

            acts = []
            for _ in range(int(head[0])):
                acts.append(input())
            print(maxMonths(head[1], acts))

    except Exception as e:
        print(e)

def maxMonths(origin, acts):
    laddus = 0
    for a in acts:
        a = a.split(" ")
        if len(a)>1:
            if a[0] == "CONTEST_WON":
                laddus += 300
                if int(a[1])<20:
                    # add bonus
                    laddus += 20-int(a[1])
            else:
                # BUG_FOUND. add severity
                laddus += int(a[1])
        else:
            if a[0] == "TOP_CONTRIBUTOR":
                laddus += 300
            else:
                laddus += 50

    if (origin=="INDIAN"):
        return laddus // 200
    else:
        return laddus // 400

main()