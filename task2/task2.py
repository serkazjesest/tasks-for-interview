from math import sqrt
x, y = float(input()), float(input())
r = float(input())
a, b = float(input()), float(input())
a += x
b += y
dist = sqrt((a ** 2) + (b ** 2))
if dist < r:
    print(1)
elif dist == r:
    print(0)
else:
    print(2)