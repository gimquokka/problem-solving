# flip cross

a = [list(map(int, input().split())) for _ in range(19)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(19):
        a[x-1][i] = 1 if a[x-1][i] == 0 else 0
        a[i][y-1] = 1 if a[i][y-1] == 0 else 0

for i in range(19):
    print(*a[i])