# Print output that last one when s is equal or large than e
e = int(input())

s = 0
n = 1

while(s < e):
	s += n

	if s >= e:
		print(n)

	n += 1

