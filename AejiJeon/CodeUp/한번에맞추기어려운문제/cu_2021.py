import sys
n = int(input())
l = []
for line in range(n):
    l.append(int(sys.stdin.readline()))

l1 = list(set(l))
c = len(l1)
lc = [l.count(l1[i]) for i in range(c)]

mx1 = max(lc)

s = lc[:]
s.remove(mx1)
mx2 = max(s)

s1 = set()
s2 = set()

for i in range(c):
    if lc[i] == mx1: s1.add(l1[i])
    if lc[i] == mx2: s2.add(l1[i])

v1 = abs(max(s1)-min(s2))
v2 = abs(min(s1)-max(s2))

print(max(v1, v2))