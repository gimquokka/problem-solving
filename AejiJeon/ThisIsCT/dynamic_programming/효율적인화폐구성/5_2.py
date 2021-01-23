n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(int(input()))

d = [10001]*(m+1)
d[0] = 0
for i in lst: 
    for j in range(i, m+1):
        d[j] = min(d[j], 1+d[j-i])
    
print(d[m] if d[m] != 10001 else -1)