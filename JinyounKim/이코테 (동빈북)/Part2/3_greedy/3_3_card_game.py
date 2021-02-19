import sys

n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]

ans = -sys.maxsize -1

for i in range(n):
	# In case of large input
	arr[i] = list(map(int, sys.stdin.readline().split()))
	arr[i].sort()
	if arr[i][0] > ans:
		ans = arr[i][0]

print(ans)
# print(sys.maxsize)

'''
모범답안
n, m = map(int, input().split())

ans = sys.maxize
for i in range(n):
	mini = min(list(map(int, sys.stdin.readline().split())))
	maxi = max(ans, mini)
'''



