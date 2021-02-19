n = int(input())
a = set(map(int, input().split()))
# a.sort()
m = int(input())
parts = list(map(int, input().split()))

'''
# Binary Search with Recursion 
def bs(a, t, s, e):
	m = (s+e)//2

	if s > e:
		return False 
	
	if t == a[m]:
		return True
	elif t > a[m]:
		return bs(a, t, m+1, e)
	else:
		return bs(a, t, s, m-1)
'''

'''
def bs(a, t, s, e):
	while s <= e:
		m= (s+e)//2

		if t == a[m]:
			return True
		elif t > a[m]:
			s = m+1
		else:
			e = m-1
	return False
'''

# results = []

for t in parts:
	if t in a:
		print('yes', end=' ')
	else: print('no', end=' ')

# print(*results)

# Check bs work!
# print(bs([1, 2, 3, 4, 5, 10], 0, 0, 5))

