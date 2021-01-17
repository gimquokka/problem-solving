m, n = map(int, input().split())

max = 0



for i in range(m):
    line = list(map(int, input().split()))
    m = min(line)
    if max < m:
        max = m

print(max)