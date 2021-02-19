import sys
from bisect import bisect_left
input = sys.stdin.readline

n, c = map(int, input().split())

a = [0]*n
for i in range(n):
	a[i] = int(input())

# from bisect import bisect_left
# a = [1,2, 4, 8, 9]
# n, c = 5, 3

def min_distance(a, c, n):
	a.sort()
	length = n
	# s = a[1] - a[0]
	# e = a[length-1] - a[0]
	gap = [0]*(n-1)
	for i in range(n-1):
		gap[i]= (a[1+i]-a[0])
	index = 0
	answer = 0
	length = len(a)
	for step in gap:
		target = a[0]+step
		prev_index = 0
		count = 1
		for i in range(c):
			index = bisect_left(a, target)
			if index != length and index != prev_index:
				count += 1
				prev_index = index
				target = a[index]+step
				if count == c:
					answer = step
					break
			else:
				return answer
	return answer

print(min_distance(a, c, n))
		
