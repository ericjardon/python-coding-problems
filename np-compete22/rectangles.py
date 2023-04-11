from sys import flags


x1, y1, x2, y2 = [float(x) for x in input().split()]


base = abs(x1-x2)
height = abs(y1-y2)

print(base*height)