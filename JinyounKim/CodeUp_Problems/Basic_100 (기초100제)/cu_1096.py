# print the board that is marked 1 with input list
n = int(input())

arr = [[0]*19 for _ in range(19)]

for _ in range(n):
	x, y = map(int, input().split())
	arr[x-1][y-1] = 1

for i in range(19):
	print(*arr[i], sep = ' ')