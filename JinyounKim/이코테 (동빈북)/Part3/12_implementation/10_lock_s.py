# 90-degree turnning matrix func
def rotate_a_matrix_by_90_degree(a):
	n = len(a)
	m = len(a[0])

	result = [[0]*m for _ in range(n)]

	for i in range(n):
		for j in range(m):
			result[j][n-1-i] = a[i][j]
	
	return result

# a = [[1, 2], [3, 4]]
# print(rotate_a_matrix_by_90_degree(a))

def check(length, new_lock):
	for i in range(length, 2*length):
		for j in range(length, 2*length):
			if new_lock[i][j] != 1:
				return False
	return True
	
	

def solution(key, lock):
	for rotate in range(4):
		key = rotate_a_matrix_by_90_degree(key)
		length = len(lock)
		length_key = len(key)
		
		# init 3-times new_lock
		new_lock = [[0]*3*length for _ in range(3*length)]
		
		for i in range(length, 2*length):
			for j in range(length, 2*length):
				new_lock[i][j] = lock[i-length][j-length]
		
		for x in range(3*length - length_key+1):   
			for y  in range(3*length - length_key+1):
				# Match Key and lock
				for i in range(length_key):
					for j in range(length_key):
						# print("x, y, i, j: ", x, y, i, j)
						new_lock[i+x][j+y] += key[i][j]
				# Check Key and lock is matched
				if check(length, new_lock) == True:
					return True
				# Remove key from lock
				for i in range(length_key):
					for j in range(length_key):
						new_lock[i+x][j+y] -= key[i][j]

	return False
				

	# print(check(length, new_lock))
    # return new_lock


# For test solution
key = [[0, 0],[0, 1]]
lock = [[1, 1], [1, 0]]
print(solution(key, lock))
