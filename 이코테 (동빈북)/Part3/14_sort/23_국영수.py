import sys
input = sys.stdin.readline

n = int(input())

a = []
for i in range(n):
	name, k, e, m = input().split()
	a.append((int(k), int(e), int(m), name))

a.sort(key = lambda x: (-x[0], x[1], -x[2], x[3]))

for i in range(n):
	print(a[i][3])