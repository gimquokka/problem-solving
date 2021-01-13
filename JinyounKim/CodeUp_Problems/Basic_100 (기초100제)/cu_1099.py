# Get maze as input and find a shorest path when repeatly move to right and left avoiding 1(block)
# If meat 2(feed) and (8,8) finish.
arr = [[0]*10 for _ in range(10)]

for i in range(10):
	arr[i] = list(map(int, input().split()))

x, y = 1, 1

for _ in range(20):
	if arr[x][y] == 2:
		# print('check')
		arr[x][y] = 9
		break
	elif arr[x][y] != 1 and arr[x][y+1] != 1:
			arr[x][y] = 9
			y += 1
	elif arr[x][y] != 1 and arr[x+1][y] != 1:
			arr[x][y] = 9
			x += 1
	else:
		arr[x][y] = 9
		break

for i in range(10):
	print(*arr[i], sep = ' ')
