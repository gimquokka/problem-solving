# import sys 
# input = sys.stdin.readline

n,c = list(map(int, input().split()))

a = [0]*n
for i in range(n):
	a[i] = int(input())
a.sort()

# n, c = 5, 3
# a = [1, 2, 4, 8, 9]

# init gap
# 이것을 1로 바꿔야함
# s = a[1] - a[0]
s = 1
e = a[-1] - a[0]

result = 0
while s <= e:
	m = (s+e)//2
	val = a[0]
	count = 1
	for i in range(1, n):
		if a[i] >= val+m:
			count += 1
			val = a[i]
	if count >= c:
		s = m+1
		result = m
	else:
		e = m-1

print(result)

