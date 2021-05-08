n = int(input())

d = [0]*n
d[0], d[1] = 1, 3

for i in range(2, n):
	d[i] = d[i-1]+2*d[i-2]

print(d[n-1]%(796796))