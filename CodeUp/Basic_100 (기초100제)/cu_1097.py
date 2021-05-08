# Get array and reverse 0 <=> 1 with cross that center point is given 
arr = [[0]*19 for _ in range(19)]

for i in range(19):
	arr[i] = list(map(int, input().split()))

# num of input coordination
n = int(input())

for _ in range(n):
	# Get input coordination n times
	x, y = map(int, input().split())
	# reverse arr along horizental x line
	for i in range(19):
		if arr[x-1][i] == 0:
			arr[x-1][i] = 1
		else:
			arr[x-1][i] = 0
	# reverse arr along vertical y line
	for j in range(19):
		if arr[j][y-1] == 0:
			arr[j][y-1] = 1
		else:
			arr[j][y-1] = 0

for i in range(19):
	print(*arr[i], sep=' ')