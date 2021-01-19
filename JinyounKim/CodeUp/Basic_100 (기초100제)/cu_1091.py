# Print r that initital value = a, and repeatly multipyly m and add d with r_n-1 for n times
a, m, d, n = map(int, input().split())

r = a
for i in range(1, n):
	r = r*m + d

print(r)
	