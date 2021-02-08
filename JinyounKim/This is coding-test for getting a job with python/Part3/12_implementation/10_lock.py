'''
Strategy

자물쇠에서 빈 부분을 정사각형으로 잘라서
4방향으로 돌리면서,
각각에 틀에 찍어보기
'''
# Extract square that contain 0
# ex) lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# Discard... It is too complex....
def get_square(lock):
	upper, left = len(lock), len(lock[0])
	bottom, right = 0, 0
	for i in range(len(lock)):
		for j in range(len(lock[0])):
			if lock[i][j] == 0:
				if i < upper:
					upper = i 
				if j < left:
					left = j
				if i > bottom:
					bottom = i
				if j > right:
					right = j
	# print(upper, bottom, left, right)
	result = [[0]*(bottom-upper+1) for _ in range(left, right+1)]

	for i in range(upper, bottom+1):
		for j in range(left, right+1):
			result[i-upper][j-left] = lock[i][j]

	return result

# get_square test code
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
# print(get_square(lock))


# 4-way rotation
def rotatate_a_matrix_by_90_degree(a):
	# Width
	n = len(a)
	# Height
	m = len(a[0])

	result = [[0]*n for _ in range(m)]
	
	for i in range(n):
		for j in range(m):
			result[j][n-1-i] = a[i][j]

	return result
# Test rotate func
#a = [[1, 2], [3, 4]]
# print(rotatate_a_matrix_by_90_degree(a))

# Check the key literaly
	l_lock = len(lock) 
	l = len(key) - l_lock
	lock = get_square(lock)

# check key and lock are matched
def check(k, l):
	l_k = len(k)
	nk = k[:]
	for i in range(l_k):
		for j in range(l_k):
			nk[i][j] += l[i][j]
			if nk[i][j] != 1:
				return False
	return True

# k = [[0, 0], [1, 0]]
# l = [[1, 1], [0, 0]]
# print(check(k, l))
		
def solution(key, lock):
	# answer = True
	lock = get_square(lock)
	for _ in range(4):
		l_l = len(lock)
		l_l1 = len(lock[0])
		l_k = len(key)
		nkey = [[0]*l_l1 for _ in range(l_l)]
		for step_i in range(l_k - l_l+1):
			for step_j in range(l_k - l_l1+1):
				for i in range(l_l):
					for j in range(l_l):
						nkey[i][j] = key[i+step_i][j+step_j]
				if check(nkey, lock) == True:
					return True
		lock = rotatate_a_matrix_by_90_degree(lock)
	return False
