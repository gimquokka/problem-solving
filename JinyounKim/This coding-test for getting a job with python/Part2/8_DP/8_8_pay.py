import sys

n, m = map(int, input().split())

a = [0]*n

for i in range(n):
	a[i] = int(sys.stdin.readline().rstrip())

d = [10001]*(m+1)
d[0] = 0
'''
for i in range(m+1):
	if i in a:
		d[i] = 1
	else:
		for j in a:
			if (0 < (i-j)) and (d[i-j] != 10001):
				d[i] = min(d[i], d[i-j] + 1)
				# d[i] = d[i-j] + 1
'''

for i in range(n):
	for j in range(a[i], m+1):
		if (d[j - a[i]] != 10001):
			d[j] = min(d[j],d[j-a[i]]+1)
print(d)
# if d[m] != 0:
# 	print(d[m])
# else: print(-1)
	

	

