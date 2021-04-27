#boj_2156
import sys
n = int(input())

wine = [0] * n
for i in range(n):
    wine[i] = int(sys.stdin.readline())

#print(wine)
d = [0] *n
d[0] =wine[0]
if n>=2:
    d[1] = wine[0] + wine[1]
if n>=3:
    d[2] = max(d[1],d[0]+wine[2],wine[1]+wine[2])
if n>=4:
    for i in range(3,n):
        d[i] = max(d[i-1],d[i-2]+wine[i], d[i-3]+wine[i-1]+wine[i])

print(d[n-1])
