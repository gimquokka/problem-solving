import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = []
for i in range(n):
    u, p = map(float, input().split())
    data.append((int(u), p))

data.sort(key=lambda x: (-x[0], x[1]))

no_happen = 1
for i in range(k):
    no_happen *= 1-data[i][1]*(0.01)

happen = 1 - no_happen
print('GG' if happen < 0.0005 else '%.3f'%(happen*100))