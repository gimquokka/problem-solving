n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(int(input()))

d = [-1]*(m+1)
d[0] = 0
for i in range(1, m+1):
    v = 10001
    
    for j in lst:
        if i-j >= 0:    
            if d[i-j] != -1:
                v = min(v, 1 + d[i-j]) 
    
    if v != 10001:
        d[i] = v

print(d[m])