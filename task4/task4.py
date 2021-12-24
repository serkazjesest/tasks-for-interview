a = [1, 2, 3]
m = sorted(a)[len(a) // 2]
print(m)
print(sum(abs(v - m) for v in a))