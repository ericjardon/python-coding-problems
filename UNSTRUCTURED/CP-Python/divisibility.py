# Reads input of the form 'n x y'
# Prints all possible ints 'a' that are divisible by x but not by y
# a is a number more than 1 and less than n
# number of t lines of input are indicated at first
# then processes input t times

t = int(input())
for i in range(t):
    # asume x < n and < is not a multiple of y
    line = str(input()).split(" ")
    n = int(line[0])
    x = int(line[1])
    y = int(line[2])
    out = ""
    for a in range(2, n):
        if a%x==0 and not(a%y==0):
            out+=str(a)
            out+=" "
    print(out.rstrip())