from math import sqrt
import sys
l, l1 = [], []
with open(sys.argv[1]) as f:
    for line in f:
        l.append(line.strip().split(' '))
with open(sys.argv[2]) as f1:
    for line in f1:
        l1.append(line.strip().split(' '))
x, y = float(l[0][0]), float(l[0][1])
r = float(l[1][0])
for i in range(0, len(l1)):
    a, b = float(l1[i][0]), float(l1[i][1])
    a += x
    b += y
    dist = sqrt((a ** 2) + (b ** 2))
    if dist < r:
        print(1)
    elif dist == r:
        print(0)
    else:
        print(2)