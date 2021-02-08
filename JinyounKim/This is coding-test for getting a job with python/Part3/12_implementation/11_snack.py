k = int(input())
n = int(input())

# add apple to map(data)
data = [[0]*(n+1) for _ in range(n+1)]
for i in range(k):
	x, y = map(int, input().split())
	data[x][y] =  1

l = int(input())

# turning info
info = []
for i in range(l):
	x, c = input().split()
	info.append((int(x), c))

# Remember this technic
def turn(sign, direction):
	if sign == 'D':
		direction = (direction+1)%4
	else:
		direction = (direction-1)%4 # Negative modulo!
	return direction

# Init place of snake
x, y = 1, 1
# Moving coordinate (East => South => West => North)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# Make a visit of starting point
data[x][y] = 2

direction = 0
index = 0
times = 0
q = []
q.append((x, y))

while True:
	times += 1

	nx = x + dx[direction]
	ny = y + dy[direction]
	# print('times, nx, ny: ', direction, times, nx, ny) # debugging용

	# 지도 안에 있고, 앞에 몸 통이 없을때
	if (1 <= nx <= n) and (1 <= ny <= n) and (data[nx][ny] != 2):
		# 사과가 없을 때만 하는 if
		if data[nx][ny] != 1:
			tail = q.pop(0)
			data[tail[0]][tail[1]] = 0 # 꼬리 지우기
		# 사과가 있을 때나 없을 때나 해야하는 것
		q.append((nx, ny))
		data[nx][ny] = 2
		x, y = nx, ny
	else: # 벽에 닿거나, 몸 통을 만나면 times 출력
		print(times)
		break
	
	# 시간이 되면 방향 회전
	if (index < l) and (times == info[index][0]):
		direction = turn(info[index][1], direction)
		index += 1
	