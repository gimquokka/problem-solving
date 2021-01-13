# Print the line with givn l(length), d (distance), x, y (coordinate) on h x w board

# Get size of board h, w
h, w = map(int, input().split())

# Initialize arr with zeros 
arr = [[0]*w for _ in range(h)]

# Get input size n
n = int(input())

# Get input 
for _ in range(n):
	l, d, x, y = map(int, input().split())
	if d == 0:
		for i in range(l):	
			arr[x-1][y-1+i] = 1
	else:
		for j in range(l):
			arr[x-1+j][y-1] = 1

# Print output
for i in range(h):
	print(*arr[i])