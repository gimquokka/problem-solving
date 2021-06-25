n, m = map(int, input().split())

ans = min(list(map(int, input().split())))
for _ in range(n-1):
    ans = max(ans, min(list(map(int, input().split()))))

print(ans)
