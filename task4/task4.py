import sys
l = []
with open(sys.argv[1]) as f:
    for line in f:
        l.append(int(line.rstrip()))
m = sorted(l)[len(l) // 2]
print(sum(abs(v - m) for v in l))