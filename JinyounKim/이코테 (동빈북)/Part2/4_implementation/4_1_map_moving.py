n = int(input())
path = list(input().split())

# x, y = 1, 1 이런식으로 그냥 활용해도 좋았을 듯
cord = [1, 1]

for dir in path:
	if dir == 'U' and (1 <= (cord[0]-1) <= n):
		cord[0] -= 1
	elif dir == 'D' and (1 <= (cord[0]+1) <= n):
		cord[0] += 1
	elif dir == 'L' and (1 <= (cord[1]-1) <= n):
		cord[1] -= 1
	elif (1 <= (cord[1]+1) <= n):
		cord[1] += 1

print(*cord)

