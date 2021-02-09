n, *size = map(int, input().split())

s = 0
e = max(size)
for i in range(10000):
    result = 1
    m = (s+e)/2
    for length in size:
        result *= length//m
    
    if result < n:
        e = m
    else:
        s = m

print("%.10f"%m)
        