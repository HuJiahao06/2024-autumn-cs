a, b = map(int, input().split())
c = {0}
for i in map(int, input().split()):
    for j in c.copy():
        if j < b: c.add(i + j)
for i in sorted(c):
    if i >= b: print(i);exit()
print(0)