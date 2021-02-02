import math
4
m, n = map(int, input().split())
Isprime = [True]*(n+1)
Isprime[1] = 0 # False

for i in range(2, int(math.sqrt(n)) + 1):
    if Isprime[i]:
        j = 2
        while i*j <= n:
            Isprime[i*j] = False
            j += 1

for i in range(m, n+1):
    if Isprime[i]:
        print(i)
