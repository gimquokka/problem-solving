def change_base(n, base):
	T = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	q, r = divmod(n, base)
	
	# Last character process
	if r == 0:
		r = 26
		q -= 1
	
	# Refer base chage method
	if q == 0:
		return T[r-1]
	else:
		return change_base(q, base) + T[r-1]


n = int(input())
print(change_base(n, 26))