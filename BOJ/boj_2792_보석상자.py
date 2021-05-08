from math import ceil
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = [0]*m
for i in range(m):
    data[i] = int(input())

e = max(data)
s = 1

while s <= e:
    count = 0
    m = (s+e)//2
    for i in data:
        count += ceil(i/m)
    
    if count > n:
        s = m+1
    # ==이 아니라 <= 이런식으로 binary search used then we can min_val
    else: 
        e = m-1
        ans = m

print(ans)