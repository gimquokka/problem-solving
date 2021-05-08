import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = []
for i in range(n):
    u, p = map(float, input().split())
    data.append((int(u), p))

data.sort(key=lambda x: (-x[0], x[1]))

answer = 0
for i in range(k):
    answer += data[i][1]

print(data)
print('GG' if answer < 0.0005 else '%.3lf' % answer)
