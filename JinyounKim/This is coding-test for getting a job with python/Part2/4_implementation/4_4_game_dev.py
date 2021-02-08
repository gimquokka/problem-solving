import sys

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

map_arr = [[0]*(m) for _ in range(n)]
visited_arr = [[0]*(m) for _ in range(n)]
visited_arr[x][y] = 1
ans_cont = 1

for i in range(n):
	map_arr[i] = list(map(int, sys.stdin.readline().rstrip().split()))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
	global direction
	direction -= 1
	if direction == -1: 
		direction = 3

turn_cont = 0

while True:
	turn_left()

	nx = x + dx[direction]
	ny = y + dy[direction]
	if (visited_arr[nx][ny] == 0) and (map_arr[nx][ny] == 0):
		visited_arr[nx][ny] = 1
		x = nx
		y = ny
		ans_cont += 1
		turn_cont = 0
		continue
	else:
		turn_cont += 1
	
	if turn_cont == 4:
		nx = x - dx[direction]
		ny = y - dy[direction]
		if (map_arr[nx][ny] == 0):
			x = nx
			y = ny
			continue
		else:
			break
		turn_cont = 0

print(ans_cont)
		
'''
while True:
	if d == 0:
		d = 3
		if 0<= y-1 <m:
			if map_arr[x][y-1] == 0:
				y -= 1
				visited.add((x, y))
			else: continue
	elif d == 1:
		d -= 1
		if 0<= x-1 <n:
			if map_arr[x-1][y] == 0:
				x -= 1
				visited.add((x, y))
			else: continue
	elif d == 2:
		d -= 1
		if 0<=y+1<m:
			if map_arr[x][y+1] == 0:
				y += 1
				visited.add((x, y))
			else: continue
	elif d == 3:
		d -= 1
		if 0<=x+1<=m:
			if map_arr[x+1][y] == 0:
				x += 1
				visited.add((x, y))
			else: continue

	news_way = [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
	# news_way_arr = [(xy in visited) for xy in news_way]
	news_land = []

	for (x, y) in news_way:
		if  (0<=x<n) and (0<=y<m):
			news_land.append(map_arr[x][y])

	if ((visited & set(news_way)) == news_way) or (0 not in news_land):
		print('check')
		if (d == 0):
			if 0<= x+1 <n:
				if map_arr[x+1][y] == 1:
					break
				else:
					x += 1
					continue 
		elif (d == 1):
			if 0<= y-1 <m:
				if map_arr[x][y-1] == 1:
					break
				else:
					y = y-1
					continue
		elif (d == 2):
			if 0<=x-1<n:
				if map_arr[x-1][y] == 1:
					break
				else:
					x -= 1 
					continue
		elif (d == 3):
			if 0<= y+1<m:
				if map_arr[x][y+1] == 1:
					break
				else: 
					y += 1
					continue

print(len(visited))
'''