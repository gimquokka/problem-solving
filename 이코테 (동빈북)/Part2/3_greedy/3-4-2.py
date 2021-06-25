n, k = map(int, input().split())

cnt = 0
while n != 1:
    n = n - 1 if n%k != 0 else n//k
    cnt += 1

print(cnt)