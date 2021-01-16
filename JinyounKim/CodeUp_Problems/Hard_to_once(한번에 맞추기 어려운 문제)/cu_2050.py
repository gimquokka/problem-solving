def remove_zero_r(a, n):	
	index = n-1

	while(index):
		# print(index)
		s = 0
		
		for j in range(index):
			s += a[j]
		
		if a[index] == 0 and s > 0:
			for k in range(index, 0, -1):
				a[k] = a[k-1]
			a[0] = 0
			index = n-1
		elif s == 0:
			return a
		else:
			index -= 1

	return a
		
def push_r(a, n):
	# while(index):
	index = n-1
	for i in range(4):
		for j in range(4-i):
			if (a[index] == a[index-1]) and (a[index] != 0):
				a[index] *= 2
				for j in range(index-1, 0, -1):
					a[j] = a[j-1]
				a[0] = 0
			index -= 1
		index = n-1
	return a

def swap_lr(a, n):
	for i in range(n):
		a[i].reverse()
	return a 

def transpose(a, n):
	a = list(map(list, zip(*a)))
	return a

def push_game(a, n, t):
	def result(a, n):
		for i in range(n):
			a[i] = remove_zero_r(a[i],n)
			a[i] = push_r(a[i],n)
		return a

	if t == 'R':
		a = result(a, n)
	elif t == 'L':
		a = swap_lr(a, n)
		a = result(a, n)
		a = swap_lr(a, n)
	elif t == 'D':
		a = transpose(a, n)
		a = result(a, n)
		a = transpose(a, n)
	elif t == 'U':
		a = transpose(a, n)
		a = swap_lr(a, n)
		a = result(a, n)
		a = swap_lr(a, n)
		a = transpose(a, n)
	return a
	
t = input()

board = [[0]*4 for _ in range(4)]
n = len(board)

for i in range(4):
	board[i] = list(map(int, input().split()))

# print(transpose(board, n))
board = push_game(board, n, t)

for i in range(n):
	print(*board[i], sep = ' ')