n = int(input())
d = list(map(int, input().split()))

m = [0]*n
m[0] = d[0]
m[1] = max(d[0], d[1])

for i in range(2, n):
	m[i] = max(m[i-1], m[i-2]+d[i])

print(m)
