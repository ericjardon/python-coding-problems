"""Golf Course
Desc) Calculate the total number of strokes a
player did in a round given the term that describes the player performance on each of the 18 holes in
the course."""

def main():
    # driver function reads the line of ordered pars
    # and runs the calculation for each of the 18 performances of golfer
    par = input().split(" ")
    strokes = 0
    for i in range(18):
        p = input()
        strokes += getStrokes(int(par[i]), p)
    print(strokes)

def getStrokes(par, performance):
    if performance == "hole in one":
        return 1
    elif performance == "condor":
        return par - 4
    elif performance == "albatross":
        return par - 3
    elif performance == "eagle":
        return par - 2
    elif performance == "birdie":
        return par - 1
    elif performance == "par":
        return par
    elif performance == "bogey":
        return par + 1
    elif performance == "double bogey":
        return par + 2
    elif performance == "triple bogey":
        return par + 3

main()